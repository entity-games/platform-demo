import Phaser from 'phaser'

import { BootScene } from './scenes/boot_scene.js'
import { LoadingScene } from './scenes/loading_scene.js'
import { MainMenuScene } from './scenes/main_menu.js'
import { StoryIntroScene } from './scenes/story_intro.js'
import { MatchmakerScene } from './scenes/matchmaker_scene.js'
import { CharacterSelectScene } from './scenes/character_select.js'
import { CharacterIntroScene } from './scenes/character_intro.js'
import { VSScene } from './scenes/vs_screen.js'
import { BattleScene } from './scenes/fight_screen.js'
import { PostFightScene } from './scenes/post_fight.js'
import { GameOverScene } from './scenes/game_over.js'

import { initScale } from './game_data/layout.js'

const config = {
  type: Phaser.AUTO,
  scale: {
    mode: Phaser.Scale.NO_CENTER,
    autoCenter: Phaser.Scale.CENTER_BOTH,
    fullscreenTarget: 'gameContainer'
  },
  parent: 'gameContainer',
  width: window.innerWidth,
  height: window.innerHeight,
  scene: [
    BootScene,
    LoadingScene,
    MainMenuScene,
    StoryIntroScene,
    MatchmakerScene,
    CharacterSelectScene,
    CharacterIntroScene,
    VSScene,
    BattleScene,
    PostFightScene,
    GameOverScene
  ]
}

const game = new Phaser.Game(config) // eslint-disable-line
initScale()

window.addEventListener('resize', () => {
  initScale()
  game.scale.resize(window.innerWidth, window.innerHeight);
});

if (window.registerGameUnloadedListener) {
  window.registerGameUnloadedListener(() => {
    console.log('RPSA: Destroying Phaser Game object...')
    game.destroy(true, true)
  })
  console.log('RPSA: Registered listener for game unloading.')
}
