package com.royaltiesInsights.enrich

import java.util.UUID
import zio._
import zio.Console.printLine
import com.royaltiesInsights.enrich.EnrichServiceRun.ApplicationLive
import com.royaltiesInsights.domain.{Location, Play, Track}
import com.royaltiesInsights.enrich.EnrichServiceRun.EnrichService
import io.getquill.jdbczio.Quill
import com.typesafe.config.ConfigFactory
import io.getquill.JdbcContextConfig
import io.getquill._
import scala.util.Try
import zio.Exit.Success

object DatabaseLayer {
  def getLocationsByCountry(countryIdentifier: String) =
    ZIO.serviceWithZIO[ApplicationLive](
      _.getLocationsByCountry(countryIdentifier)
    )
  def getAllLocations() =
    ZIO.serviceWithZIO[ApplicationLive](_.getAllLocations())
  def getAllTracks() = ZIO.serviceWithZIO[ApplicationLive](_.getAllTracks())
  def getAllPlays() =
    ZIO.serviceWithZIO[ApplicationLive](_.getAllPlays())
  def insertPlay(play: Play) =
    ZIO.serviceWithZIO[ApplicationLive](_.insertPlay(play))
}

object EnrichDatabase extends ZIOAppDefault {
  def getRandomPlayer = {
    for {
      existingLocations <- DatabaseLayer.getAllLocations()
      existingTracks <- DatabaseLayer.getAllTracks()
      _ <- ZIO
        .fail(new Exception("No locations available!"))
        .when(existingLocations.isEmpty)
      _ <- ZIO
        .fail(new Exception("No tracks available!"))
        .when(existingTracks.isEmpty)

      randomLocation <- Random.nextIntBetween(0, existingLocations.length - 1)
      randomTrack <- Random.nextIntBetween(0, existingTracks.length - 1)
      randomPlayedMs <- Random.nextIntBetween(0, 600000)
      selectedLocation: Location = existingLocations(randomLocation)
      selectedTrack: Track = existingTracks(randomTrack)
      newPlay: Play = Play(
        selectedLocation.id,
        selectedTrack.id,
        randomPlayedMs
      )
      _ <- DatabaseLayer.insertPlay(newPlay)
    } yield newPlay
  }

  def run = {
    val dataServiceLive = ZLayer.fromFunction(EnrichService.apply _)
    val applicationLive = ZLayer.fromFunction(ApplicationLive.apply _)
    val dataSourceLive = Quill.DataSource.fromJdbcConfigClosable(
      JdbcContextConfig(ConfigFactory.parseString("""
        dataSourceClassName = "org.postgresql.ds.PGSimpleDataSource"
        dataSource.url = "jdbc:postgresql://ep-orange-darkness-a2al3uis.eu-central-1.aws.neon.tech/neondb"
        dataSource.user = "neondb_owner"
        dataSource.password = "Y4G0PaUwdkgH"
      """))
    )
    val postgresLive = Quill.Postgres.fromNamingStrategy(Literal)

    (for {
      _ <- Console.printLine("Starting random play generation...")
      * <- ZIO.foreachDiscard(1 to 100000)(* =>
        getRandomPlayer
          .tap(play => Console.printLine(s"Inserted play: $play"))
      )
      _ <- Console.printLine("Finished generating plays")
    } yield ()).provide(
      applicationLive,
      dataServiceLive,
      dataSourceLive,
      postgresLive
    )
  }
}
