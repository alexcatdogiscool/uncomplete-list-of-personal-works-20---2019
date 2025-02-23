import sys
import pygame as pg


pg.init()
screen = pg.display.set_mode((640, 480))

# The original image.
IMAGE = pg.Surface((250, 250), pg.SRCALPHA)
IMAGE.fill(pg.Color('springgreen1'))
pg.draw.rect(IMAGE, (50, 90, 120), (10, 10, 60, 60))

IMAGE_SMALL = pg.transform.rotozoom(IMAGE, 0, .2)
# Create an image with lower alpha and blit it on the small image
# with the BLEND_RGBA_MULT special_flag to make it transparent.
alpha_img = pg.Surface(IMAGE_SMALL.get_rect().size, pg.SRCALPHA)
alpha_img.fill((255, 255, 255, 127))
IMAGE_SMALL.blit(alpha_img, (0, 0), special_flags=pg.BLEND_RGBA_MULT)


def main():
    clock = pg.time.Clock()
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        screen.fill((70, 70, 70))
        pg.draw.circle(screen, (240, 170, 0), (300, 240), 140)
        screen.blit(IMAGE, (30, 30))
        screen.blit(IMAGE_SMALL, (400, 260))

        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()
    pg.quit()
    sys.exit()
