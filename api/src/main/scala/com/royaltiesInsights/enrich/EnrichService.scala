package com.royaltiesInsights.enrich

import io.getquill._
import zio._
import zio.Console.printLine
import java.sql.SQLException
import io.getquill.jdbczio.Quill
import java.util.UUID
import com.typesafe.config.ConfigFactory
import com.royaltiesInsights.domain.{Location, Play, Track}

object EnrichServiceRun {
  case class EnrichService(quill: Quill.Postgres[Literal]) {
    import quill._
    val locations = quote(query[Location])
    val tracks = quote(query[Track])
    val plays = quote(query[Play])

    def locationByCountry = quote((countryIdentifier: String) =>
      locations.filter(location => location.country == countryIdentifier)
    )

    def tracksByLicensor = quote((licensor: String) =>
      tracks.filter(track => track.licensor == licensor)
    )

    def playsByTrack = quote((trackid: UUID) =>
      plays.filter(play => play.trackid == trackid)
    )

    def playsByLocation = quote((locationid: UUID) =>
      plays.filter(play => play.locationid == locationid)
    )

    def insertPlay =
      quote((play: Play) => plays.insertValue(play))

    def insertTrack = quote((track: Track) => tracks.insertValue(track))

    def insertLocation = quote((location: Location) => locations.insertValue(location))

  }

  case class ApplicationLive(dataService: EnrichService) {
    import dataService.quill.{run => quillRun, _}

    def getLocationsByCountry(
        countryIndentifier: String
    ): ZIO[Any, SQLException, List[Location]] = quillRun(
      dataService.locationByCountry(lift(countryIndentifier))
    )

    def getTracksByLicensor(
        licensor: String
    ): ZIO[Any, SQLException, List[Track]] = quillRun(
      dataService.tracksByLicensor(lift(licensor))
    )

    def getPlaysByTrack(trackUUID: UUID): ZIO[Any, SQLException, List[Play]] =
      quillRun(
        dataService.playsByTrack(lift(trackUUID))
      )

    def getPlaysByLocation(
        locationUUID: UUID
    ): ZIO[Any, SQLException, List[Play]] = quillRun(
      dataService.playsByLocation(lift(locationUUID))
    )

    def getAllLocations(): ZIO[Any, SQLException, List[Location]] = quillRun(
      dataService.locations
    )

    def getAllTracks(): ZIO[Any, SQLException, List[Track]] = quillRun(
      dataService.tracks
    )

    def getAllPlays(): ZIO[Any, SQLException, List[Play]] = quillRun(
      dataService.plays
    )

    def insertPlay(play: Play): ZIO[Any, SQLException, Long] =
      quillRun(
        dataService.insertPlay(lift(play))
      )
  }

}
