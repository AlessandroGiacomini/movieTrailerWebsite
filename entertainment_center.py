import media
import fresh_tomatoes


# Instances of some movies
gladiator = media.Movie("Gladiator",
                        "When a Roman general is betrayed and his family murdered by an emperor's corrupt son, he comes to Rome as a gladiator to seek revenge.",
                        "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
                        "https://www.youtube.com/watch?v=IvTT29cavKo")

good_will_hunting = media.Movie("Good Will Hunting",
                    "Will Hunting, a janitor at M.I.T., has a gift for mathematics, but needs help from a psychologist to find direction in his life.",
                    "https://upload.wikimedia.org/wikipedia/en/b/b8/Good_Will_Hunting_theatrical_poster.jpg",
                    "https://www.youtube.com/watch?v=QSMvyuEeIyw")

meet_joe_black = media.Movie("Meet Joe Black",
                    "Death, who takes the form of a young man, asks a media mogul to act as a guide to teach him about life on Earth and in the process he falls in love with his guide's daughter.",
                    "https://upload.wikimedia.org/wikipedia/en/f/f5/Meet_Joe_Black-_1998.jpg",
                    "https://www.youtube.com/watch?v=_zIOjl93WrU")

interstellar = media.Movie("Interstellar",
                    "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
                    "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                    "https://www.youtube.com/watch?v=0vxOhd4qlnA")

the_wizard_of_oz = media.Movie("The Wizard of Oz",
                    "Dorothy Gale is swept away to a magical land in a tornado and embarks on a quest to see the Wizard who can help her return home.",
                    "https://upload.wikimedia.org/wikipedia/commons/c/ca/WIZARD_OF_OZ_ORIGINAL_POSTER_1939.jpg",
                    "https://www.youtube.com/watch?v=vkZcYMy85lY")

pulp_fiction = media.Movie("Pulp Fiction",
                    "The lives of two mob hit men, a boxer, a gangster's wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
                    "https://upload.wikimedia.org/wikipedia/en/8/82/Pulp_Fiction_cover.jpg",
                    "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

man_of_steel = media.Movie("Man of Steel",
                    "Clark Kent, one of the last of an extinguished race disguised as an unremarkable human, is forced to reveal his identity when Earth is invaded by an army of survivors who threaten to bring the planet to the brink of destruction.",
                    "https://upload.wikimedia.org/wikipedia/en/8/85/ManofSteelFinalPoster.jpg",
                    "https://www.youtube.com/watch?v=T6DJcgm3wNY")

the_truman_show = media.Movie("The Truman Show",
                    "An insurance salesman/adjuster discovers his entire life is actually a television show",
                    "https://upload.wikimedia.org/wikipedia/en/c/cd/Trumanshow.jpg",
                    "https://www.youtube.com/watch?v=c3gI9ms8Fdc")

finding_nemo = media.Movie("Finding Nemo",
                    "After his son is captured in the Great Barrier Reef and taken to Sydney, a timid clownfish sets out on a journey to bring him home.",
                    "https://upload.wikimedia.org/wikipedia/en/2/29/Finding_Nemo.jpg",
                    "https://www.youtube.com/watch?v=SPHfeNgogVs")

movies = [good_will_hunting,meet_joe_black,interstellar,man_of_steel,
          finding_nemo,the_wizard_of_oz,gladiator,the_truman_show,pulp_fiction]

# open the web page with the movies
fresh_tomatoes.open_movies_page(movies)
