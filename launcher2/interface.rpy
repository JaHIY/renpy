# This file contains the various components of the launcher interface.

init python:

    # Settings.
    config.developer = True
    
    # Style customizations
    style.window.yminimum = 60
    style.window.left_padding = 60
        
    tooltip = "Welcome!"

    def show_tooltip(st, at):
        return Text(tooltip, color="#fff", size=14), None

    def set_tooltip(s):
        global tooltip
        
        if tooltip != s:
            tooltip = s
            renpy.restart_interaction()

    tooltips = renpy.curry(set_tooltip)

    def unset_tooltip(s):
        global tooltip

        if s and tooltip == s:
            tooltip = ""
            renpy.restart_interaction()

    untooltips = renpy.curry(unset_tooltip)
            
            
    def screen():
        """
         Display a screen. This should be called before any code that
         draws to the screen.
         """
        
        ui.add(Solid("#fff"))
        
        ui.window(yalign=1.0)
        ui.add(DynamicDisplayable(show_tooltip))

        ui.image("eileen_small.png", xalign=0.0, yalign=1.0)
        
        ui.window(xmargin=20, top_margin=4, bottom_margin=85, style='default')
        
    def interact():
        """
         Closes the screen, and causes an interaction to occur.
         """
        
        return ui.interact(suppress_overlay=True, suppress_underlay=True)

    def title(s):
        """
         Display a title on the screen.
         """

        ui.window(style="default", bottom_margin=4, top_margin=12)
        ui.text(s, size=26, color="#333", font="DejaVuSerif.ttf")
                
    def text(s):
        """
         Display text on the screen.
         """
        
        ui.text(s, size=15, color="#333", font="DejaVuSerif.ttf", justify=True)
        
    def button(s, clicked=None, subtitle=""):
        """
         Displays a button with caption `s`.
         """

        ui.button(style="default", clicked=clicked,
                  hovered=tooltips(subtitle), unhovered=untooltips(subtitle),
                  top_padding=3, bottom_padding=3)

        ui.text(s, style="default", size=20,
                color="#06c", hover_color="00c", insensitive_color="#aaa",
                font="DejaVuSerif.ttf", minwidth=250)
        
    def scrolled(cancel, **kwargs):

        yadj = ui.adjustment()

        ui.side(['r', 'b', 'c'])

        ui.bar(adjustment=yadj, style='vscrollbar')
        
        if cancel:
            ui.vbox()
            ui.null(height=12)
            button(_("Cancel"), clicked=ui.jumps(cancel))
            ui.close()
        else:
            ui.null()               
                    
        ui.viewport(yadjustment=yadj, mousewheel=True)

        # Left up to the user to close.