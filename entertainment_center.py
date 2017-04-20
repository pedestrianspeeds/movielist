import fresh_tomatoes
import media
import webbrowser

# modules founds within same file tree
# 15 objects, each is its own movie object

breathless = media.Movie("Breathless (A bout de souffle)",
                         # storyline taken from imdb.com
                         # http://www.imdb.com/title/tt0053472/
                         "A thief impulsively murders a motorcycle policeman.",
                         # img provided is the main image on wikipedia page
                         # https://upload.wikimedia.org/wikipedia/en/thumb/f/fe/1961_Une_femme_est_une_femme.jpg/220px-1961_Une_femme_est_une_femme.jpg# "https://upload.wikimedia.org/wikipedia/en/thumb/3/3f/%C3%80_bout_de_souffle_%28movie_poster%29.jpg/220px-%C3%80_bout_de_souffle_%28movie_poster%29.jpg
                         "https://goo.gl/O4CLKJ",
                         # movie trailer provided for free on youtube.com
                         "https://www.youtube.com/watch?v=2K-0JGUo0qA")

le_petit_soldat = media.Movie("Le Petit Soldat",
                              # http://www.imdb.com/title/tt0054177/
                              "A young Frenchman lives in Geneva",
                              # "https://upload.wikimedia.org/wikipedia/en/thumb/a/a0/Le_Petit_Soldat.jpg/220px-Le_Petit_Soldat.jpg
                              "https://goo.gl/7Y6E4A",
                              "https://www.youtube.com/watch?v=SS1qNnW3XF8")

une_femme_est_une_femme = media.Movie("Une Femme Est Une Femme",
                                      # http://www.imdb.com/title/tt0055572/
                                      "An artist is desperate to be a mother",
                                      # https://upload.wikimedia.org/wikipedia/en/thumb/f/fe/1961_Une_femme_est_une_femme.jpg/220px-1961_Une_femme_est_une_femme.jpg
                                      "goo.gl/oHr4O9",
                                      "https://goo.gl/DC9Qss")

vivre_sa_vie = media.Movie("Vivre Sa Vie",
                           # http://www.imdb.com/title/tt0056663
                           "Twelve tales in the life of a Parisian woman",
                           # https://upload.wikimedia.org/wikipedia/en/9/97/VivresaViePoster.jpg
                           "https://goo.gl/a86nro",
                           "https://www.youtube.com/watch?v=ZAZGR5O33jw")

les_carabiniers = media.Movie("Les Carabiniers",
                              # http://www.imdb.com/title/tt0056905
                              "A war in an imaginary country",
                              # https://images-na.ssl-images-amazon.com/images/M/MV5BMTYxNjQwMjI4N15BMl5BanBnXkFtZTcwNTg3ODMyMQ@@._V1_UY268_CR4,0,182,268_AL_.jpg
                              "https://goo.gl/NLYlN6",
                              "https://www.youtube.com/watch?v=hpoXoyO_KHE")

le_mepris = media.Movie("Le Mepris",
                        # http://www.imdb.com/title/tt0057345
                        "Paul's marriage to his wife Camille disintegrates",
                        # https://upload.wikimedia.org/wikipedia/en/thumb/1/15/1963_Le_mepris_1.jpg/220px-1963_Le_mepris_1.jpg
                        "https://goo.gl/zi1fwt",
                        "https://www.youtube.com/watch?v=72xGErvgStM")

band_of_outsiders = media.Movie("Bande a Part",
                                # http://www.imdb.com/title/tt0057869/
                                "Two crooks commit a robbery",
                                # https://upload.wikimedia.org/wikipedia/en/5/5d/Band_a_Part_French_poster.jpg
                                "https://goo.gl/0PH1bg",
                                "https://www.youtube.com/watch?v=TM0lC2QCiSU")

une_femme_mariee = media.Movie("Une Femme Mariee",
                               # http://www.imdb.com/title/tt0058701
                               "Charlotte is young and modern",
                               # https://upload.wikimedia.org/wikipedia/en/thumb/5/55/AMarriedWoman1964Poster.jpg/220px-AMarriedWoman1964Poster.jpg
                               "https://goo.gl/x13DqS",
                               "https://www.youtube.com/watch?v=g3_Z3vsdjKk")

alphaville = media.Movie("Alphaville",
                         # http://www.imdb.com/title/tt0058898
                         "A secret agent is sent to Alphaville",
                         # https://upload.wikimedia.org/wikipedia/en/a/ad/Alphaville1965.jpg
                         "https://goo.gl/Hu9z0E",
                         "https://www.youtube.com/watch?v=UQCic5WTx-o")

pierrot_le_fou = media.Movie("Pierrot Le Fou",
                             # http://www.imdb.com/title/tt0059592
                             "Pierrot escapes his society",
                             # https://upload.wikimedia.org/wikipedia/en/thumb/a/a9/Pierrotlefouposter.jpg/220px-Pierrotlefouposter.jpg
                             "https://goo.gl/LeicJt",
                             "https://www.youtube.com/watch?v=ycg2yb3qiUo")

masculin_feminin = media.Movie("Masculin Feminin",
                               # http://www.imdb.com/title/tt0060675
                               "Paul is disillusioned with civilian life",
                               # https://upload.wikimedia.org/wikipedia/en/thumb/1/1d/Masculinf%C3%A9minin.jpg/220px-Masculinf%C3%A9minin.jpg
                               "https://goo.gl/ElE9PY",
                               "https://www.youtube.com/watch?v=53KROTcwf-Y")

made_in_usa = media.Movie("Made in U.S.A.",
                          # http://www.imdb.com/title/tt0060647
                          "Paula goes from Paris to the town",
                          # https://upload.wikimedia.org/wikipedia/en/thumb/4/4d/Made_usa.jpg/220px-Made_usa.jpg
                          "https://goo.gl/UPuD9X",
                          "https://www.youtube.com/watch?v=8K-X2B_Cvqs")

two_or_three = media.Movie("Two or Three Things I Know About Her",
                           # http://www.imdb.com/title/tt0060304
                           "Her is Juliette and the actress playing her",
                           # https://upload.wikimedia.org/wikipedia/en/thumb/f/f1/TwoorthreethingsPoster.jpg/220px-TwoorthreethingsPoster.jpg
                           "https://goo.gl/X0z2Cq",
                           "https://www.youtube.com/watch?v=UjRlMX01_4A")

la_chinoise = media.Movie("La Chinoise",
                          # http://www.imdb.com/title/tt0061473
                          "A group of French students are studying Mao",
                          # https://upload.wikimedia.org/wikipedia/en/thumb/a/a8/La_Chinoise_Australian_DVD_cover.jpg/220px-La_Chinoise_Australian_DVD_cover.jpg
                          "https://goo.gl/0V45lZ",
                          "https://www.youtube.com/watch?v=SFaEY92jGHI")

week_end = media.Movie("Week End",
                       # http://www.imdb.com/title/tt0062480
                       "A week-end trip turns into a traffic jam",
                       # https://upload.wikimedia.org/wikipedia/en/thumb/6/65/Weekendflm.jpg/220px-Weekendflm.jpg
                       "https://goo.gl/iFDMvw",
                       "https://www.youtube.com/watch?v=dFJLuhVvBPM")

# call movies on fresh_tomatoes template,
# resulting in a complete webpage with capability to view trailers
movies = {breathless, le_petit_soldat, une_femme_est_une_femme,
          vivre_sa_vie, les_carabiniers, le_mepris, band_of_outsiders,
          une_femme_mariee, alphaville, pierrot_le_fou, masculin_feminin,
          made_in_usa, two_or_three, la_chinoise, week_end}
fresh_tomatoes.open_movies_page(movies)
