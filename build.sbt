scalaVersion := "2.12.18"

name := "scala-spark-template"
organization := "com.example"
version := "1.0"

libraryDependencies ++= Seq(
  "dev.zio" %% "zio" % "2.1.14",
  "dev.zio" %% "zio-sql-postgres" % "0.1.2",
  "com.github.ghostdogpr" %% "caliban" % "2.8.1",
  "com.github.ghostdogpr" %% "caliban-quick" % "2.8.1", // Optional: HTTP routes via ZIO HTTP
  "io.getquill" %% "quill-jdbc-zio" % "4.8.5",
  "org.postgresql" % "postgresql" % "42.3.1"
)

fork := true
