<template>
  <div id="app">
    <div class="player">
      <div class="options">
        <div class="option">
          <input type="checkbox" id="animal" name="animal" checked>
          <label for="animal" class="icon"><img src="./assets/options/animal.png" /></label>
        </div>
        <br>
        <div class="option">
          <input type="checkbox" id="attribute" name="attribute">
          <label for="attribute" class="icon"><img src="./assets/options/attribute.png" /></label>
        </div>
        <br>
        <div class="option">
          <input type="checkbox" id="color" name="color">
          <label for="color" class="icon"><img src="./assets/options/color.png" /></label>
        </div>
      </div>
      <div class="control">
        <button class="play" v-if="!isPlaying" @click="play"> <img src="./assets/icons/play.svg" class="play_img" />
        </button>
        <button class="pause" v-else @click="pause"> <img src="./assets/icons/pause.svg" class="pause_img" />
        </button><br>
        <button class="intro" @click="intro"> <img src="./assets/icons/intro.svg" class="intro_img" /> </button>
      </div>
    </div>
    <div class="playlist">
      <button v-for="song in animalAssets" :key="song.sound" @click="playSong(song)" class="icon">
        <img :src="song.image" />
      </button>
      <br>
      <button v-for="song in attributeAssets" :key="song.sound" @click="playSong(song)" class="icon">
        <img :src="song.image" />
      </button>
      <br>
      <button v-for="song in colorAssets" :key="song.sound" @click="playSong(song)" class="icon">
        <img :src="song.image" />
      </button>
    </div>
  </div>
</template>

<script>

export default {
  name: 'app',
  data() {
    return {
      current: {},
      toBePlayed: [],
      playAnimals: true,
      playAttributes: false,
      playColors: false,
      isPlaying: false,
      animalAssets: [
        {
          title: 'cat',
          sound: require('./assets/animals/cat.mp3'),
          image: require('./assets/animals/cat.png'),
        },
        {
          title: 'cow',
          sound: require('./assets/animals/cow.mp3'),
          image: require('./assets/animals/cow.png'),
        },
        {
          title: 'elephant',
          sound: require('./assets/animals/elephant.mp3'),
          image: require('./assets/animals/elephant.png'),
        },
        {
          title: 'snake',
          sound: require('./assets/animals/snake.mp3'),
          image: require('./assets/animals/snake.png'),
        },
      ],
      attributeAssets: [
        {
          title: 'boots',
          sound: require('./assets/attributes/boots.mp3'),
          image: require('./assets/attributes/boots.png'),
        },
        {
          title: 'glasses',
          sound: require('./assets/attributes/glasses.mp3'),
          image: require('./assets/attributes/glasses.png'),
        },
        {
          title: 'hat',
          sound: require('./assets/attributes/hat.mp3'),
          image: require('./assets/attributes/hat.png'),
        },
        {
          title: 'umbrella',
          sound: require('./assets/attributes/umbrella.mp3'),
          image: require('./assets/attributes/umbrella.png'),
        },
      ],
      colorAssets: [
        {
          title: 'blue',
          sound: require('./assets/colors/blue.mp3'),
          image: require('./assets/colors/blue.png'),
        },
        {
          title: 'green',
          sound: require('./assets/colors/green.mp3'),
          image: require('./assets/colors/green.png'),
        },
        {
          title: 'red',
          sound: require('./assets/colors/red.mp3'),
          image: require('./assets/colors/red.png'),
        },
        {
          title: 'yellow',
          sound: require('./assets/colors/yellow.mp3'),
          image: require('./assets/colors/yellow.png'),
        },
      ],
      player: new Audio()
    }
  },
  methods: {
    getImagePath(type, name) {
      return './assets/' + type + '/' + name + '.png'
    },
    getRandom(array) {
      return array[Math.floor(Math.random() * array.length)];
    },
    playSong(song) {
      if (song != undefined && song.sound != undefined) {
        this.current = song;
        this.player.src = this.current.sound;
      } else {
        this.current = this.toBePlayed.shift();
        this.player.src = this.current.sound;
      }
      console.log(this.current.title);
      this.player.play();
      this.isPlaying = true;
    },
    play() {
      if (this.toBePlayed.length === 0) {
        if (document.querySelector('#animal').checked) {
          this.toBePlayed.push(this.getRandom(this.animalAssets));
        }
        if (document.querySelector('#attribute').checked) {
          this.toBePlayed.push(this.getRandom(this.attributeAssets));
        }
        if (document.querySelector('#color').checked) {
          this.toBePlayed.push(this.getRandom(this.colorAssets));
        }
      }
      this.playSong();
    },
    pause() {
      this.player.pause();
      this.isPlaying = false;
    },
    intro() {
      this.toBePlayed = [...this.animalAssets, ...this.attributeAssets, ...this.colorAssets];
      this.playSong();
    }
  },
  created() {

    this.player.addEventListener('ended', function () {
      this.isPlaying = false;
      console.log(this.toBePlayed.length);
      if (this.toBePlayed.length > 0) {
        setTimeout(function () { this.playSong() }.bind(this), 10);  // 2000
      }
    }.bind(this));
  },
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

#app {
  display: flex;
  flex-direction: column;
  width: 100%;
  align-items: center;
}

body {
  font-family: sans-serif;
}

.icon {
  width: 54px;
  height: 54px;
  padding: 1px;
  margin: 5px 12px;
  border-width: 1px;
  border-top-width: 1px;
  border-right-width: 1px;
  border-bottom-width: 1px;
  border-left-width: 1px;
  background: transparent;
  border-radius: 5%;
  border-top-left-radius: 5%;
  border-top-right-radius: 5%;
  border-bottom-right-radius: 5%;
  border-bottom-left-radius: 5%;
}

input {
  width: 30px;
  margin: 10px 10px 20px 0px;
}

.option {
  display: flex;
  flex-direction: row;
}

.player {
  display: flex;
  align-items: center;
}

.play,
.pause {
  font-size: 120px;
  border: 0;
  background: transparent;
}

.play_img {
  margin: 25px 0 0 0;
  width: 160px;
  background: #16c60c;
  border-radius: 5%;
}

.pause_img {
  margin: 25px 0 0 0;
  width: 160px;
  background: #e81224;
  border-radius: 5%;
}

.intro {
  margin: -50px 0 10px 0;
  width: 160px;
  height: 40px;
  border: 0;
  background: #0078d7;
  border-radius: 5%;
}

.options {
  padding: 10px;
  margin-top: 30px;
}
</style>
