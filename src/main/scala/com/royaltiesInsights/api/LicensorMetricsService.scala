package com.royaltiesInsights.api

import io.getquill._
import zio._
import zio.Console.printLine
import java.sql.SQLException
import io.getquill.jdbczio.Quill
import java.util.UUID
import com.typesafe.config.ConfigFactory
import com.royaltiesInsights.domain.{
  Location,
  Play,
  Track,
  MarketSharePerCountry,
  TopTrackPerCountry,
  TopTracks,
  TotalPlayedTime
}

sealed class LicensorMetricsService(
    quill: Quill.Postgres[Literal],
    licensorUUID: UUID
) {
  import quill._

  private val countryMarketShareQuery = quote {
    query[MarketSharePerCountry].filter(_.licensorUUID == lift(licensorUUID))
  }

  private val topTrackPerCountryQuery = quote {
    query[TopTrackPerCountry].filter(_.licensorUUID == lift(licensorUUID))
  }

  private val topTracksQuery = quote {
    query[TopTracks].filter(_.licensorUUID == lift(licensorUUID))
  }

  private val totalPlayedTimeQuery = quote {
    query[TotalPlayedTime].filter(_.licensorUUID == lift(licensorUUID))
  }

  def getCountryMarketShare
      : ZIO[Any, SQLException, List[MarketSharePerCountry]] =
    quill.run(countryMarketShareQuery)

  def getTopTrackPerCountry: ZIO[Any, SQLException, List[TopTrackPerCountry]] =
    quill.run(topTrackPerCountryQuery)

  def getTopTracks: ZIO[Any, SQLException, List[TopTracks]] =
    quill.run(topTracksQuery)

  def getTotalPlayedTime: ZIO[Any, SQLException, List[TotalPlayedTime]] =
    quill.run(totalPlayedTimeQuery)
}
