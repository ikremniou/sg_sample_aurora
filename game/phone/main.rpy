define sg_phone.style.width = 491
define sg_phone.style.height = 1042
define sg_phone.active_screen = "sg_aurora_screen"
define sg_phone.time = "1:30 AM"
define sg_aurora.bgcolor = "#161616"
define sg_aurora.style.post_padding = 12

transform sg_phone_active_area():
    offset (15, 51)
    xysize (465, 940) 

transform sg_phone_apper_from_buttom(time):
    on show:
        pos (0.5, 1.0)
        anchor (0.5, 0.0)
        ease time align(0.5, 0.5)
    on hide:
        ease time pos(0.5, 1.0) anchor (0.5, 0.0)

transform sg_phone_zoom_image(time):
    on show:
        zoom 0.0
        ease time zoom (1.0)
    on hide:
        zoom 1.0
        ease time zoom (0.0)

transform sg_phone_header_iconbox:
    size (18, 14)

screen sg_aurora():
    modal True
    add Solid("#D3D3D3")
    fixed at sg_phone_apper_from_buttom(1):
        xysize (sg_phone.style.width, sg_phone.style.height)
        fixed at sg_phone_active_area:
            vbox:
                use sg_phone_header(sg_phone, sg_aurora.bgcolor)
                use expression sg_phone.active_screen pass (sg_aurora)
        add Frame("frame")

    textbutton "Return" action Return(0)

screen sg_phone_header(sg_phone, color):
    fixed:
        ysize 34
        add Solid(color)
        hbox:
            xoffset 12
            align (0.0, 0.5)
            text sg_phone.time:
                size 12
                bold True
                color "#FFFFFF"

        hbox:
            xoffset -12
            spacing 8
            align (1.0, 0.5)
            add "battery" at sg_phone_header_iconbox
            add "wifi" at sg_phone_header_iconbox
            add "connection" at sg_phone_header_iconbox

style post_text_style:
    color "#FFFFFF"
    size 14

style post_follow_text_style:
    color "#FFFFFF"
    align (0.5, 0.5)
    bold True
    size 12

style post_character_name_style:
    color "#FFFFFF"
    size 22

style post_character_followers_style:
    color "#525252"
    bold True
    size 14

style post_liked_text_style:
    color "#FFFFFF"
    size 14

screen sg_aurora_zoom_picture_screen(picture):
    imagebutton at sg_phone_zoom_image(0.3):
        align (0.5, 0.5)
        idle picture
        action Hide("sg_aurora_zoom_picture_screen")

screen sg_aurora_screen(sg_aurora):
    fixed:
        add Solid(sg_aurora.bgcolor)
        viewport:
            spacing 10
            xsize 1.0
            draggable True
            mousewheel True
            vbox:
                fixed:
                    ysize 50
                    add "app_logo":
                        align (0.5, 0.5)
                for post in sg_aurora.recent_posts:
                    null height 10
                    vbox:
                        ysize 85
                        spacing 10
                        add "split_line_2":
                            xalign (0.5)
                        hbox:
                            xoffset sg_aurora.style.post_padding
                            spacing 10
                            add post.character.picture:
                                size (65, 65)
                            fixed:
                                vbox:
                                    text post.character.name:
                                        style "post_character_name_style"
                                    null height 10
                                    frame:
                                        background None
                                        padding (0, 0, 0, 0)
                                        xysize (80, 30)
                                        if post.character.is_followed_by_mc:
                                            imagebutton:
                                                idle "unfollow"
                                                align (0.5, 0.5)
                                                action SetField(post.character, "is_followed_by_mc", False)
                                            text "Unfollow":
                                                style "post_follow_text_style"
                                        else:
                                            imagebutton:
                                                idle "follow"
                                                align (0.5, 0.5)
                                                action SetField(post.character, "is_followed_by_mc", True)
                                            text "Follow":
                                                style "post_follow_text_style"

                                text post.character.followers:
                                    xoffset -sg_aurora.style.post_padding * 2
                                    align (1.0, 0.5)
                                    style "post_character_followers_style"
                        text post.text:
                            xoffset sg_aurora.style.post_padding
                            style "post_text_style"

                        imagebutton:
                            idle sg_aurora.FitByWidth(post.picture)
                            action Show("sg_aurora_zoom_picture_screen", None, post.picture)

                        fixed:
                            yfit True
                            vbox:
                                frame:
                                    background None
                                    xpadding sg_aurora.style.post_padding
                                    ysize 32
                                    hbox:
                                        spacing 20
                                        align (0.0, 0.5)
                                        if not post.is_liked_by_mc:
                                            imagebutton:
                                                idle "like"
                                                action Function(post.mcLikePost)
                                        else:
                                            imagebutton:
                                                idle "unlike"
                                                action Function(post.mcLikePost)
                                        add "comment"
                                        add "share"
                                    hbox:
                                        align (1.0, 0.0)
                                        add "bookmark"
                                frame:
                                    background None
                                    xpadding sg_aurora.style.post_padding
                                    vbox:
                                        spacing 5
                                        if post.likes is not None:
                                            text "Liked by {b}[post.likes].{/b}":
                                                style "post_text_style"
                                        else:
                                            text "Liked by {b}[post.likes_with]{/b} and {b}[post.likes] others.{/b}":
                                                style "post_text_style"
                                        $ comments_size = len(post.comments)
                                        text "{b}[comments_size] Comments{/b}":
                                            style "post_text_style"
        imagebutton:
            align (0.5, 0.98)
            idle "home_button"
            action Return(0)
