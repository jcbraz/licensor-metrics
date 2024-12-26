package com.royaltiesInsights.domain

import java.util.UUID

final case class Play(locationid: UUID, trackid: UUID, playedMs: Int);
