file://<WORKSPACE>/src/main/scala/com/royaltiesInsights/enrich/DataService.scala
### scala.reflect.internal.Types$TypeError: illegal cyclic inheritance involving trait ParIterable

occurred in the presentation compiler.

presentation compiler configuration:
Scala version: 2.12.18
Classpath:
<WORKSPACE>/.bloop/royalties-insights-api/bloop-bsp-clients-classes/classes-Metals-NbjCIMomS9qnA1BsrDzLxg== [exists ], <HOME>/Library/Caches/bloop/semanticdb/com.sourcegraph.semanticdb-javac.0.10.3/semanticdb-javac-0.10.3.jar [exists ], <HOME>/.sbt/boot/scala-2.12.18/lib/scala-library.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/dev/zio/zio_2.12/2.1.14/zio_2.12-2.1.14.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/io/getquill/quill-jdbc-zio_2.12/4.8.5/quill-jdbc-zio_2.12-4.8.5.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/postgresql/postgresql/42.3.1/postgresql-42.3.1.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/dev/zio/zio-internal-macros_2.12/2.1.14/zio-internal-macros_2.12-2.1.14.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/dev/zio/zio-stacktracer_2.12/2.1.14/zio-stacktracer_2.12-2.1.14.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/dev/zio/izumi-reflect_2.12/2.3.10/izumi-reflect_2.12-2.3.10.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/io/getquill/quill-zio_2.12/4.8.5/quill-zio_2.12-4.8.5.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/io/getquill/quill-sql_2.12/4.8.5/quill-sql_2.12-4.8.5.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/io/getquill/quill-jdbc_2.12/4.8.5/quill-jdbc_2.12-4.8.5.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/scala-lang/modules/scala-collection-compat_2.12/2.12.0/scala-collection-compat_2.12-2.12.0.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/zaxxer/HikariCP/6.2.1/HikariCP-6.2.1.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/dev/zio/zio-json_2.12/0.7.3/zio-json_2.12-0.7.3.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/checkerframework/checker-qual/3.37.0/checker-qual-3.37.0.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/dev/zio/izumi-reflect-thirdparty-boopickle-shaded_2.12/2.3.10/izumi-reflect-thirdparty-boopickle-shaded_2.12-2.3.10.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/io/getquill/quill-core_2.12/4.8.5/quill-core_2.12-4.8.5.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/dev/zio/zio-streams_2.12/2.1.12/zio-streams_2.12-2.1.12.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/io/getquill/quill-engine_2.12/4.8.5/quill-engine_2.12-4.8.5.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/softwaremill/magnolia1_2/magnolia_2.12/1.1.10/magnolia_2.12-1.1.10.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/typesafe/config/1.4.3/config-1.4.3.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/dev/zio/zio-logging_2.12/2.4.0/zio-logging_2.12-2.4.0.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/typesafe/scala-logging/scala-logging_2.12/3.9.5/scala-logging_2.12-3.9.5.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/github/takayahilton/sql-formatter_2.12/1.2.1/sql-formatter_2.12-1.2.1.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/io/suzaku/boopickle_2.12/1.5.0/boopickle_2.12-1.5.0.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/lihaoyi/pprint_2.12/0.9.0/pprint_2.12-0.9.0.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/github/ben-manes/caffeine/caffeine/3.1.8/caffeine-3.1.8.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/dev/zio/zio-parser_2.12/0.1.10/zio-parser_2.12-0.1.10.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/dev/zio/zio-prelude_2.12/1.0.0-RC33/zio-prelude_2.12-1.0.0-RC33.jar [exists ], <HOME>/.sbt/boot/scala-2.12.18/lib/scala-reflect.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/slf4j/slf4j-api/1.7.36/slf4j-api-1.7.36.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/lihaoyi/fansi_2.12/0.5.0/fansi_2.12-0.5.0.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/lihaoyi/sourcecode_2.12/0.4.0/sourcecode_2.12-0.4.0.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/google/errorprone/error_prone_annotations/2.21.1/error_prone_annotations-2.21.1.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/dev/zio/zio-prelude-macros_2.12/1.0.0-RC33/zio-prelude-macros_2.12-1.0.0-RC33.jar [exists ]
Options:
-Yrangepos -Xplugin-require:semanticdb


action parameters:
offset: 1053
uri: file://<WORKSPACE>/src/main/scala/com/royaltiesInsights/enrich/DataService.scala
text:
```scala
package com.royaltiesInsights.enrich

import io.getquill._
import zio._
import zio.Console.printLine
import java.sql.SQLException
import io.getquill.jdbczio.Quill
import java.util.UUID
import com.typesafe.config.ConfigFactory

object DataServiceRun extends ZIOAppDefault {
  case class DataService(quill: Quill.Postgres[Literal]) {
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

    def playsByTrack = quote((trackUUID: UUID) =>
      plays.filter(play => play.trackUUID == trackUUID)
    )

    def playsByLocation = quote((locationUUID: UUID) =>
      plays.filter(play => play.locationUUID == locationUUID)
    )

    def insertLocations = quote((locationValues: List[Location]) => locationValues.@@)
  }

  case class ApplicationLive(dataService: DataService) {
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
  }

  object Application {
    def getLocationsByCountry(countryIdentifier: String) =
      ZIO.serviceWithZIO[ApplicationLive](
        _.getLocationsByCountry(countryIdentifier)
      )
    def getAllPlays() =
      ZIO.serviceWithZIO[ApplicationLive](_.getAllPlays())
  }

  def run = {
    val dataServiceLive = ZLayer.fromFunction(DataService.apply _)
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
      allPlays <- Application.getAllPlays()
      _ <- printLine(allPlays.toString)
    } yield ()).provide(
      applicationLive,
      dataServiceLive,
      dataSourceLive,
      postgresLive
    )
  }

}

```



#### Error stacktrace:

```

```
#### Short summary: 

scala.reflect.internal.Types$TypeError: illegal cyclic inheritance involving trait ParIterable