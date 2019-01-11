import media
import fresh_tomatoes

# Creating nine movies with their attributes

theInvisibleGuest = media.Movie()
theInvisibleGuest.trailer_youtube_url = \
    "https://www.youtube.com/watch?v=epCg2RbyF80"
theInvisibleGuest.poster_image_url = \
    "http://www.gstatic.com/tv/thumb/v22vodart/13287373/p13287373_v_v8_an.jpg"
theInvisibleGuest.title = "The Invisible Guest"
Movies = [theInvisibleGuest]

beforeSunRise = media.Movie()
beforeSunRise.trailer_youtube_url = \
    "https://www.youtube.com/watch?v=25v7N34d5HE"
beforeSunRise.poster_image_url = \
    "http://www.gstatic.com/tv/thumb/v22vodart/16390/p16390_v_v8_aa.jpg"
beforeSunRise.title = "Before Sunrise"
Movies.append(beforeSunRise)

beforeSunSet = media.Movie()
beforeSunSet.trailer_youtube_url = \
    "https://www.youtube.com/watch?v=oY0oJc3H_bs"
beforeSunSet.poster_image_url = \
    "http://www.gstatic.com/tv/thumb/v22vodart/34625/p34625_v_v8_aa.jpg"
beforeSunSet.title = "Before Sunset"
Movies.append(beforeSunSet)

aboutTime = media.Movie()
aboutTime.trailer_youtube_url = \
    "https://www.youtube.com/watch?v=T7A810duHvw"
aboutTime.poster_image_url = \
    "http://www.gstatic.com/tv/thumb/v22vodart/9564054/p9564054_v_v8_ad.jpg"
aboutTime.title = "About Time"
Movies.append(aboutTime)

theProposal = media.Movie()
theProposal.trailer_youtube_url = \
    "https://www.youtube.com/watch?v=V3JpKPZkC2w"
theProposal.poster_image_url = \
    "http://www.gstatic.com/tv/thumb/v22vodart/192250/p192250_v_v8_ac.jpg"
theProposal.title = "The Proposal"
Movies.append(theProposal)

friendsWithBenefits = media.Movie()
friendsWithBenefits.trailer_youtube_url = \
    "https://www.youtube.com/watch?v=vLmNvYTTWXM"
friendsWithBenefits.poster_image_url = \
    "http://www.gstatic.com/tv/thumb/v22vodart/8405003/p8405003_v_v8_ab.jpg"
friendsWithBenefits.title = "Friends With Benefits"
Movies.append(friendsWithBenefits)

noStringsAttached = media.Movie()
noStringsAttached.trailer_youtube_url = \
    "https://www.youtube.com/watch?v=X7bRikS7C3o"
noStringsAttached.poster_image_url =\
    "http://www.gstatic.com/tv/thumb/v22vodart/8369331/p8369331_v_v8_ai.jpg"
noStringsAttached.title = "No Strings Attached"
Movies.append(noStringsAttached)

murderOnTheOrientExpress = media.Movie()
murderOnTheOrientExpress.trailer_youtube_url = \
    "https://www.youtube.com/watch?v=LPxZRmiXGao"
murderOnTheOrientExpress.poster_image_url = \
    "http://www.gstatic.com/tv/thumb/v22vodart/14119324/p14119324_v_v8_ac.jpg"
murderOnTheOrientExpress.title = "Murder On The Orient Express"
Movies.append(murderOnTheOrientExpress)

rampage = media.Movie()
rampage.trailer_youtube_url = \
    "https://www.youtube.com/watch?v=coOKvrsmQiI"
rampage.poster_image_url = \
    "https://images-na.ssl-images-amazon.com/images/I/51CWmgcwyVL.jpg"
rampage.title = "Rampage"
Movies.append(rampage)

fresh_tomatoes.open_movies_page(Movies)
