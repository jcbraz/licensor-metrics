package com.royaltiesInsights.domain

import java.util.UUID

// interesting metrics for licensors
    // market share per country
    // most played track belonging to licensor per country
    // total amount of played time (hours)
    // top 5 tracks played

final case class MarketSharePerCountry(
    licensorUUID: UUID,
    country: String,
    marketShare: Float
);

final case class TopTrackPerCountry(
    licensorUUID: UUID,
    country: String,
    track: String
);

final case class TopTracks(
    licensorUUID: UUID,
    tracks: List[String]
);

final case class TotalPlayedTime(
    licensorUUID: UUID,
    totalPlayTime: Float
);
