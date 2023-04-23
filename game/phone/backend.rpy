
init python in sg_aurora:
    recent_posts = []
    from store import Transform

    class FitByWidth(renpy.Displayable):

        def __init__(self, child, **kwargs):
            super(FitByWidth, self).__init__(**kwargs)
            self.child = renpy.displayable(child)

        def render(self, width, height, st, at):
            child_render = renpy.render(self.child, width, height, st, at)
            c_width, c_height = child_render.get_size();
            t = Transform(self.child, zoom=width/c_width);
            return renpy.render(t, width, height, st, at)

        def event(self, ev, x, y, st):
            return self.child.event(ev, x, y, st)

        def visit(self):
            return [ self.child ]

    class AuroraCharacter:
        def __init__(self, name, followers, picture, is_followed_by_mc):
            self.name = name
            self.followers = followers
            self.picture = picture
            self.is_followed_by_mc = is_followed_by_mc

    class AuroraPost:
        def __init__(self, character, text, picture, likes, likes_with, is_bookmarked):
            self.character = character
            self.text = text
            self.picture = picture
            self.likes = likes
            self.likes_with = likes_with
            self.is_bookmarked = is_bookmarked
            self.comments = []
            self.is_liked_by_mc = False
        
        def mcLikePost(self):
            if self.is_liked_by_mc:
                self.likes -= 1;
                self.is_liked_by_mc = False
            else:
                self.likes += 1;
                self.is_liked_by_mc = True

    characters = {
        "bella": AuroraCharacter(name="Bellchen", followers = "14K Followers", picture = "ph_circle", is_followed_by_mc=False)
    }

    def addPostBy(character_id, text, picture, likes=0, likes_with=None, is_bookmarked=False):
        global characters

        character = characters[character_id]
        new_post = AuroraPost(character, text, picture, likes, likes_with, is_bookmarked);

        recent_posts.append(new_post)
        pass

