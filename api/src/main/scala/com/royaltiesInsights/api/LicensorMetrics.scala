package com.royaltiesInsights.api

import io.getquill._
import zio._
import zio.Console.printLine
import java.sql.SQLException
import io.getquill.jdbczio.Quill
import java.util.UUID
import com.typesafe.config.ConfigFactory
import com.royaltiesInsights.domain.{
  MarketSharePerCountry,
  TopTrackPerCountry,
  TopTracks,
  TotalPlayedTime
}

object LicensorMetricsRun extends ZIOAppDefault {
  def run: ZIO[Any, Throwable, Unit] = {
    val licensorUUID = UUID.fromString("your-licensor-uuid-here")

    val dataSourceLayer = Quill.DataSource.fromPrefix("your.datasource.prefix")
    val postgresLayer = Quill.Postgres.fromNamingStrategy(Literal)

    val metricsServiceLayer =
      ZLayer.fromFunction((quill: Quill.Postgres[Literal]) =>
        new LicensorMetricsService(quill, licensorUUID)
      )

    (for {
      service <- ZIO.service[LicensorMetricsService]
      countryMarketShare <- service.getCountryMarketShare
      _ <- printLine(s"Country Market Share: $countryMarketShare")
      topTrackPerCountry <- service.getTopTrackPerCountry
      _ <- printLine(s"Top Track Per Country: $topTrackPerCountry")
      topTracks <- service.getTopTracks
      _ <- printLine(s"Top Five Tracks: $topTracks")
      totalPlayedTime <- service.getTotalPlayedTime
      _ <- printLine(s"Top Five Tracks: $totalPlayedTime")
    } yield ()).provide(
      dataSourceLayer,
      postgresLayer,
      metricsServiceLayer
    )
  }
}
