file://<WORKSPACE>/src/main/scala/com/royaltiesInsights/enrich/EnrichDatabase.scala
### scala.reflect.internal.Types$TypeError: illegal cyclic reference involving object Predef

occurred in the presentation compiler.

presentation compiler configuration:
Scala version: 2.12.18
Classpath:
<WORKSPACE>/.bloop/royalties-insights-api/bloop-bsp-clients-classes/classes-Metals-WkQgwrgGTFS4D0XVKKunRg== [exists ], <HOME>/Library/Caches/bloop/semanticdb/com.sourcegraph.semanticdb-javac.0.10.3/semanticdb-javac-0.10.3.jar [exists ], <HOME>/.sbt/boot/scala-2.12.18/lib/scala-library.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/dev/zio/zio_2.12/2.1.14/zio_2.12-2.1.14.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/io/getquill/quill-jdbc-zio_2.12/4.8.5/quill-jdbc-zio_2.12-4.8.5.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/postgresql/postgresql/42.3.1/postgresql-42.3.1.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/dev/zio/zio-internal-macros_2.12/2.1.14/zio-internal-macros_2.12-2.1.14.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/dev/zio/zio-stacktracer_2.12/2.1.14/zio-stacktracer_2.12-2.1.14.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/dev/zio/izumi-reflect_2.12/2.3.10/izumi-reflect_2.12-2.3.10.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/io/getquill/quill-zio_2.12/4.8.5/quill-zio_2.12-4.8.5.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/io/getquill/quill-sql_2.12/4.8.5/quill-sql_2.12-4.8.5.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/io/getquill/quill-jdbc_2.12/4.8.5/quill-jdbc_2.12-4.8.5.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/scala-lang/modules/scala-collection-compat_2.12/2.12.0/scala-collection-compat_2.12-2.12.0.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/zaxxer/HikariCP/6.2.1/HikariCP-6.2.1.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/dev/zio/zio-json_2.12/0.7.3/zio-json_2.12-0.7.3.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/checkerframework/checker-qual/3.37.0/checker-qual-3.37.0.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/dev/zio/izumi-reflect-thirdparty-boopickle-shaded_2.12/2.3.10/izumi-reflect-thirdparty-boopickle-shaded_2.12-2.3.10.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/io/getquill/quill-core_2.12/4.8.5/quill-core_2.12-4.8.5.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/dev/zio/zio-streams_2.12/2.1.12/zio-streams_2.12-2.1.12.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/io/getquill/quill-engine_2.12/4.8.5/quill-engine_2.12-4.8.5.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/softwaremill/magnolia1_2/magnolia_2.12/1.1.10/magnolia_2.12-1.1.10.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/typesafe/config/1.4.3/config-1.4.3.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/dev/zio/zio-logging_2.12/2.4.0/zio-logging_2.12-2.4.0.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/typesafe/scala-logging/scala-logging_2.12/3.9.5/scala-logging_2.12-3.9.5.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/github/takayahilton/sql-formatter_2.12/1.2.1/sql-formatter_2.12-1.2.1.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/io/suzaku/boopickle_2.12/1.5.0/boopickle_2.12-1.5.0.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/lihaoyi/pprint_2.12/0.9.0/pprint_2.12-0.9.0.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/github/ben-manes/caffeine/caffeine/3.1.8/caffeine-3.1.8.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/dev/zio/zio-parser_2.12/0.1.10/zio-parser_2.12-0.1.10.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/dev/zio/zio-prelude_2.12/1.0.0-RC33/zio-prelude_2.12-1.0.0-RC33.jar [exists ], <HOME>/.sbt/boot/scala-2.12.18/lib/scala-reflect.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/slf4j/slf4j-api/1.7.36/slf4j-api-1.7.36.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/lihaoyi/fansi_2.12/0.5.0/fansi_2.12-0.5.0.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/lihaoyi/sourcecode_2.12/0.4.0/sourcecode_2.12-0.4.0.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/google/errorprone/error_prone_annotations/2.21.1/error_prone_annotations-2.21.1.jar [exists ], <HOME>/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/dev/zio/zio-prelude-macros_2.12/1.0.0-RC33/zio-prelude-macros_2.12-1.0.0-RC33.jar [exists ]
Options:
-Yrangepos -Xplugin-require:semanticdb


action parameters:
offset: 126
uri: file://<WORKSPACE>/src/main/scala/com/royaltiesInsights/enrich/EnrichDatabase.scala
text:
```scala
package com.royaltiesInsights.enrich

import java.util.UUID
import zio._

object EnrichDatabase extends ZIOAppDefault {

    C@@
}
```



#### Error stacktrace:

```

```
#### Short summary: 

scala.reflect.internal.Types$TypeError: illegal cyclic reference involving object Predef