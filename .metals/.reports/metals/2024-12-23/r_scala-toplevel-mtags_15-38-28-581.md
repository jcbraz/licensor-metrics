error id: file://<WORKSPACE>/src/main/scala/com/royaltiesInsights/enrich/DataService.scala:[475..475) in Input.VirtualFile("file://<WORKSPACE>/src/main/scala/com/royaltiesInsights/enrich/DataService.scala", "package com.royaltiesInsights.enrich
import io.getquill._
import zio.ZIO
import java.sql.SQLException
import io.getquill.jdbczio.Quill

case class DataService(quill: Quill.Postgres[Literal]) {
    import quill._
    val locations = quote(query[Location])
    val tracks = quote(query[Track])
    val plays = quote(query[Play])
    def locationByCountry = quote((countryIdentifier: String) => locations.filter(location => location.country == countryIdentifier))
}

case class ")
file://<WORKSPACE>/file:<WORKSPACE>/src/main/scala/com/royaltiesInsights/enrich/DataService.scala
file://<WORKSPACE>/src/main/scala/com/royaltiesInsights/enrich/DataService.scala:15: error: expected identifier; obtained eof
case class 
           ^
#### Short summary: 

expected identifier; obtained eof