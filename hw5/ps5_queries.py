#
# CS 460: Problem Set 5: MongoDB Query Problems
#

#
# For each query, use a text editor to add the appropriate XQuery
# command between the triple quotes provided for that query's variable.
#
# For example, here is how you would include a query that finds
# the names of all movies in the database from 1990.
#
sample = """
    db.movies.find( { year: 1990 }, 
                    { name: 1, _id: 0 } )
"""

#
# 1. Put your query for this problem between the triple quotes found below.
#    Follow the same format as the model query shown above.
#
query1 = """
    db.people.find(
        { pob: / Florida, USA/ },
        { name: 1, pob: 1, _id: 0 }
    )
"""

#
# 2. Put your query for this problem between the triple quotes found below.
#
query2 = """
    db.movies.find(
        { year: 2023, earnings_rank: { $exists: true } },
        { name: 1, earnings_rank: 1, _id: 0 }
    )
"""

#
# 3. Put your query for this problem between the triple quotes found below.
#
query3 = """
    db.movies.find(
        {"actors.name": "Julianne Moore"},
        {name: 1, year: 1, rating: 1, _id: 0}
    )
"""

#
# 4. Put your query for this problem between the triple quotes found below.
#
query4 = """
    db.oscars.find(
        {type: "BEST-PICTURE", year: {$gte: 2020}},
        {"movie.name": 1, year: 1, _id: 0}
    )
"""

#
# 5. Put your query for this problem between the triple quotes found below.
#
query5 = """
    db.people.count({
        hasDirected: true, 
        $or: [
                { dob: /-11-/ }, 
                { dob: /-12-/ }
            ]
        }
    )
"""
# db.people.aggregate(
#         {
#             $match: {
#                 hasDirected: true, 
#                 $or: [
#                     { dob: /-11-/ }, 
#                     { dob: /-12-/ }
#                 ]
#             }
#         },
#         {
#             $group: {
#                 _id: null, 
#                 count: { $sum: 1 }
#             }
#         },
#         {
#             $project: {
#                 _id: 0,
#                 count: "$count"
#             }
#         }
        
#     )


#
# 6. Put your query for this problem between the triple quotes found below.
#
query6 = """
    db.movies.aggregate(
        {
            $sort: {runtime: 1}
        },
        {
            $limit: 1
        },
        {
            $project: {_id: 0, name: 1, runtime: 1}
        }
    )
"""

#
# 7. Put your query for this problem between the triple quotes found below.
#
query7 = """
    db.oscars.aggregate(
        {
            $group: 
            {
                _id: "$movie.id", 
                movie: { $first: "$movie.name" },
                types: {$push: "$type"}, 
                num_awards:{$sum: 1}
            }            
        },
        {
            $match: {num_awards: {$gte: 4}}
        },
        {
            $project: 
            {
                _id: 0, 
                types: 1,
                num_awards: 1, 
                movie: 1,
            }
        }
    )
"""

#
# 8. Put your query for this problem between the triple quotes found below.
#
query8 = """
    db.movies.aggregate(
        {
            $match: {year: {$lte: 2020, $gte: 2010}}
        },
        {
            $group: 
            {
                _id: "$year", 
                avg_runtime: {$avg: "$runtime"}, 
                best_rank: {$min: "$earnings_rank"}, 
                num_movies: {$sum:1}
            }
        },
        {
            $sort: {_id: 1}
        },
        {
            $project:
            {
                _id: 0,
                year: "$_id",
                num_movies: 1,
                avg_runtime: 1,
                best_rank: 1
            }
        }
    )
"""

#
# 9. Put your query for this problem between the triple quotes found below.
#
query9 = """
    db.movies.aggregate(
        {
            $unwind: "$actors"
        },
        {
            $match: {genre: /N/}
        },
        {
            $group: {_id: "$actors.name", num_animated: {$sum: 1}}
        },
        {
            $match: {num_animated: {$gte: 3}}
        },
        {
            $sort: {num_animated: -1, _id: 1}
        },
        {
            $project: {_id: 0, actor: "$_id", num_animated: 1}
        }
    )
"""

#
# 10. Put your query for this problem between the triple quotes found below.
#
query10 = """
    db.people.aggregate(
        {
            $match: {pob: {$exists: true}}
        },
        {
            $group: 
                {
                    _id:  {$arrayElemAt: [{ $split: ["$pob", ", "] }, -1] },
                    num_born: {$sum: 1}
                } 
        },
        {
            $sort: {num_born: -1}
        },
        {
            $limit: 5
        },
        {
            $project: {_id: 0, num_born: 1, country: "$_id"}
        }
    )
"""
