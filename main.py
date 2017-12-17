import pygame
from manageScenes import SceneManager

"""decided to change my main framework because this one made more sense to me;
link: https://stackoverflow.com/questions/14700889/pygame-level-menu-states"""
class PygameGame(object):
    
    def init(self):
        pass

    def __init__(self, width=800, height=600, fps=50, title="There Will Be Sheep"):
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        pygame.init()

    def run(self):
        manager = SceneManager()
        
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height))
        
        # set the title of the window
        pygame.display.set_caption(self.title)
        # call game-specific initialization
        self.init()
        playing = True
        
        while playing: 
            time = clock.tick(self.fps)
            manager.scene.handle_events()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    playing = False      
            manager.scene.timerFired(time)
            manager.scene.update()
            manager.scene.render(screen)
            pygame.display.flip()
        pygame.quit()

def main():
    game = PygameGame()
    game.run()

if __name__ == '__main__':
    main()