/*
 * MovieToXML
 * 
 * A class for objects that are able to convert movie data from the 
 * relational database used in PS 1 to XML.
 */

import java.sql.*;      // needed for the JDBC-related classes
import java.io.*;       // needed for the PrintStream class

public class MovieToXML {
    private Connection db;   // a connection to the database
    
    /*
     * MovieToXML constructor - takes the name of a SQLite file containing
     * a Movie table like the one from PS 1, and creates an object that 
     * can be used to convert the data in that table to XML.
     * 
     * ** YOU SHOULD NOT CHANGE THIS METHOD **
     */
    public MovieToXML(String dbFilename) throws SQLException {
        this.db = DriverManager.getConnection("jdbc:sqlite:" + dbFilename);
    }
    
    /*
     * simpleElem - a private helper method takes the name and value of 
     * a simple XML element and returns a string representation of that 
     * element
     * 
     * ** YOU SHOULD NOT CHANGE THIS METHOD **
     */
    private String simpleElem(String name, String value) {
        String elem = "<" + name + ">";
        elem += value;
        elem += "</" + name + ">";
        return elem;
    }
    
    /*
     * Takes a string representing a SQL query for the movie database
     * and returns a ResultSet object that represents the results
     * of the query (if any).
     * 
     * ** YOU SHOULD NOT CHANGE THIS METHOD **
     */
    public ResultSet resultsFor(String query) throws SQLException {
        Statement stmt = this.db.createStatement();
        ResultSet results = stmt.executeQuery(query);
        return results;
    }

    /*
     * idFor - takes the name of a movie and returns the id number of 
     * that movie in the database as a string. If the movie is not in the 
     * database, it returns an empty string.
     * 
     * ** YOU SHOULD NOT CHANGE THIS METHOD **
     */
    public String idFor(String name) throws SQLException {
        String query = "SELECT id FROM Movie WHERE name = '" + name + "';";
        ResultSet results = resultsFor(query);
        
        if (results.next()) {    
            String id = results.getString(1);
            return id;
        } else {
            return "";
        }
    }   
    
    /*
     * fieldsFor - takes a string representing the id number of a movie
     * and returns a sequence of XML elements for the non-null field values
     * of that movie in the database. If there is no movie with the specified
     * id number, the method returns an empty string.
     */
    public String fieldsFor(String movieID) throws SQLException {
        
        // replace this return statement with your implementation of the method
        if (movieID == null || movieID.equals("")){
            return "";
        }
        String query = "SELECT * FROM Movie WHERE id = '" + movieID + "';";
        ResultSet results = resultsFor(query);
        // String[] data = new String[6];
        String[] attribute_ls = {"name", "year", "rating", "runtime", "genre", "earnings_rank"};
        String result = "";
        if (results.next()) {   
            for(int i=0; i<attribute_ls.length; i++) {
                String data = results.getString(attribute_ls[i]);
                if(data != null){
                    result += "    " + simpleElem(attribute_ls[i], data)+ "\n";
                }
                
            } 
        } 
        else {
            return "";
        }
        return result;
    }
    
    /*
     * actorsFor - takes a string representing the id number of a movie
     * and returns a single complex XML element named "actors" that contains a
     * nested child element named "actor" for each actor associated with that
     * movie in the database. If there is no movie with the specified
     * id number, the method returns an empty string.
     */
    public String actorsFor(String movieID) throws SQLException {
        
        // replace this return statement with your implementation of the method
        if (movieID == null || movieID.equals("")){
            return "";
        }
        // System.out.println(movieID);
        String query = "SELECT P.name\n" + //
                "FROM Movie M, Actor A, Person P\n" + //
                "WHERE A.movie_id = M.id \n" + //
                "AND A.actor_id = P.id\n" + //
                "AND M.id = '" + movieID + "'\n" + //
                "ORDER BY P.name;";
        ResultSet results = resultsFor(query);
        String result = "";
        while(results.next()) {
            result += "      " + simpleElem("actor", results.getString("name")) + "\n";
        }
        if(result.equals("")){
            return "";
        }
        else {
            result = "    <actors>\n" + result;
            result += "    </actors>\n";
            return result;
        }
    }    
    
    /*
     * directorsFor - takes a string representing the id number of a movie
     * and returns a single complex XML element named "directors" that contains a
     * nested child element named "director" for each director associated with 
     * that movie in the database. If there is no movie with the specified
     * id number, the method returns an empty string.
     */
    public String directorsFor(String movieID) throws SQLException {
        
        // replace this return statement with your implementation of the method
        if (movieID == null || movieID.equals("")){
            return "";
        }
        // System.out.println(movieID);
        String query = "SELECT P.name\n" + //
                "FROM Movie M, Director D, Person P\n" + //
                "WHERE D.movie_id = M.id \n" + //
                "AND D.director_id = P.id\n" + //
                "AND M.id = '" + movieID + "'\n" + //
                "ORDER BY P.name;";
        ResultSet results = resultsFor(query);
        String result = "";
        while(results.next()) {
            result += "      " + simpleElem("director", results.getString("name")) + "\n";
        }
        if(result.equals("")){
            return "";
        }
        else {
            result = "    <directors>\n" + result;
            result += "    </directors>\n";
            return result;
        }
    }    
    
    /*
     * elementFor - takes a string representing the id number of a movie
     * and returns a single complex XML element named "movie" that contains
     * nested child elements for all of the fields, actors, and directors 
     * associated with  that movie in the database. If there is no movie with 
     * the specified id number, the method returns an empty string.
     */
    public String elementFor(String movieID) throws SQLException {
        if (movieID == "" || movieID == null){
            return "    <actors>\n";
        }
        String result = "";
        String fieldElement = fieldsFor(movieID);
        String directorElement = directorsFor(movieID);
        String actorElement = actorsFor(movieID);

        result += fieldElement+actorElement+directorElement;

        if(result.equals("")) {
            return "";
        }
        else {
            result = "  <movie id=\""+ movieID+"\">\n" + result;
            result += "  </movie>\n";
            return result;
        }
    }

    /*
     * createFile - creates a text file with the specified filename containing 
     * an XML representation of the entire Movie table.
     * 
     * ** YOU SHOULD NOT CHANGE THIS METHOD **
     */
    public void createFile(String filename) 
      throws FileNotFoundException, SQLException 
    {
        PrintStream outfile = new PrintStream(filename);    
        outfile.println("<?xml version=\"1.0\" encoding=\"iso-8859-1\"?>");
        outfile.println("<movies>");
        
        // Use a query to get all of the ids from the Movie Table.
        ResultSet results = resultsFor("SELECT id FROM Movie;");
        
        // Process one movie id at a time, creating its 
        // XML element and writing it to the output file.
        while (results.next()) {
            String movieID = results.getString(1);
            outfile.println(elementFor(movieID));
        }
        
        outfile.println("</movies>");
        
        // Close the connection to the output file.
        outfile.close();
        System.out.println("movies.xml has been written.");
    }
    
    /*
     * closeDB - closes the connection to the database that was opened when 
     * the MovieToXML object was constructed
     * 
     * ** YOU SHOULD NOT CHANGE THIS METHOD **
     */
    public void closeDB() throws SQLException {
        this.db.close();
    }

    /*** YOU SHOULD NOT CHANGE THIS METHOD ***/
    public static void main(String[] args) 
        throws ClassNotFoundException, SQLException, FileNotFoundException
    {
        MovieToXML xml = new MovieToXML("movie.sqlite");
        xml.createFile("movies.xml");
        xml.closeDB();
    }
}
