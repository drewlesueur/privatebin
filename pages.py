import access

def posts_page(posts, user):    
    ret = "<h2>PrivateBin</h2>"
    ret += "Post here (the url in your address bar) to log, and visit this same page to see posts. "
    ret += "<br/><b>"+ user.nickname() + "</b> " + access.logout_link() + "<br />"
    for post in posts:
        ret = ret + "created: " + str(post.created) + "<br />"
        ret = ret + "post: " + str(post.post) + "<br />"
        ret += "<hr/ >"
    ret += "<div>Please contact <a href = 'http://twitter.com/drewlesueur'>Drew LeSueur</a> for help etc.</div>" 
    ret += "<a href = 'http://github.com/drewlesueur/privatebin'>See source code</a>"   
    return ret
