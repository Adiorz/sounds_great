<template>
  <div id="app">
    <div class="player">
      <div class="options">
        <div class="option">
          <input type="checkbox" id="animal" name="animal" checked>
          <label for="animal" class="icon"><img :src="iconAssets.animal" /></label>
        </div>
        <br>
        <div class="option">
          <input type="checkbox" id="attribute" name="attribute">
          <label for="attribute" class="icon"><img :src="iconAssets.attribute" /></label>
        </div>
        <br>
        <div class="option">
          <input type="checkbox" id="color" name="color">
          <label for="color" class="icon"><img :src="iconAssets.color" /></label>
        </div>
      </div>
      <div class="control">
        <button class="play" v-if="!isPlaying" @click="play">
          <svg class="play_img" width="160" height="160" xmlns="http://www.w3.org/2000/svg" fill="white">
            <g>
              <title>play</title>
              <path stroke="null" id="svg_1"
                d="m43.17908,40.60063l0,78.79874c0,6.00878 7.01719,9.65969 12.42123,6.38909l65.65506,-39.39937c5.00075,-2.96636 5.00075,-9.81181 0,-12.85423l-65.65506,-39.32331c-5.40404,-3.2706 -12.42123,0.3803 -12.42123,6.38909z" />
              <text transform="matrix(7.90178 0 0 5.50952 -620.323 -624.598)" stroke="#000" xml:space="preserve"
                text-anchor="start" font-family="'Caveat'" font-size="5" id="svg_2" y="140.07375" x="90.14896"
                stroke-width="0" fill="white">play</text>
            </g>
          </svg>
        </button>
        <button class="pause" v-else @click="pause">
          <svg class="pause_img" width="160" height="160" xmlns="http://www.w3.org/2000/svg" fill="white">
            <g>
              <title>pause</title>
              <path stroke="null"
                d="m50.11833,124.30675c8.21746,0 14.94083,-5.69658 14.94083,-12.65907l0,-63.29535c0,-6.96249 -6.72338,-12.65907 -14.94083,-12.65907s-14.94083,5.69658 -14.94083,12.65907l0,63.29535c0,6.96249 6.72338,12.65907 14.94083,12.65907zm44.82251,-75.95443l0,63.29535c0,6.96249 6.72338,12.65907 14.94083,12.65907s14.94083,-5.69658 14.94083,-12.65907l0,-63.29535c0,-6.96249 -6.72338,-12.65907 -14.94083,-12.65907s-14.94083,5.69658 -14.94083,12.65907z"
                id="svg_1" />
              <text transform="matrix(7.90178 0 0 5.50952 -620.323 -624.598)" stroke="#000" xml:space="preserve"
                text-anchor="start" font-family="'Caveat'" font-size="5" id="svg_2" y="140.07375" x="88.14896"
                stroke-width="0" fill="white">pause</text>
            </g>
          </svg>
        </button><br>
        <button class="intro" @click="intro">
          <div><img :src="iconAssets.intro" class="intro_img" title="intro" /></div>
          <div><text class="intro_text" style="font-family='Caveat'">intro</text></div>
        </button>
      </div>
    </div>
    <div class="playlist">
      <button v-for="song in animalAssets" :key="song.sound" @click="playSong(song)"
        class="icon">
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
      isPlaying: false,
      timeout: 2000,
      iconAssets: {
        "intro": require('./assets/icons/intro.svg'),
        "animal": require('./assets/options/animal.png'),
        "attribute": require('./assets/options/attribute.png'),
        "color": require('./assets/options/color.png'),
      },
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
      player: new Audio(),
      intro_player: new Audio(),
    }
  },
  methods: {
    getRandom(array) {
      return array[Math.floor(Math.random() * array.length)];
    },
    playSong(song) {
      if (song != undefined && song.sound != undefined) {
        this.current = song;
      } else {
        this.current = this.toBePlayed.shift();
      }
      if (this.current === undefined) {
        console.log("No song to be played.")
        return null;
      }
      console.log(this.current.title);
      this.player.src = this.current.sound;
      this.player.play();
      this.isPlaying = true;
    },
    shuffle(originalArray) {
      // Do not modify original array, work on its copy
      var array = [].concat(originalArray);
      let currentIndex = array.length, randomIndex;

      // While there remain elements to shuffle.
      while (currentIndex != 0) {

        // Pick a remaining element.
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex--;

        // And swap it with the current element.
        [array[currentIndex], array[randomIndex]] = [
          array[randomIndex], array[currentIndex]];
      }

      return array;
    },
    play() {
      console.log("Play!");
      this.timeout = 2000;
      var toBePlayed = [];
      var playAnimals = document.querySelector('#animal').checked;
      var playAttributes = document.querySelector('#attribute').checked;
      var playColors = document.querySelector('#color').checked;
      if (this.toBePlayed.length === 0) { // do not add new songs for multiple play buttons
        for (let i = 0; i < 100; i++) {
          // Use chunk of toBePlayed that contains all possible items selected. 
          // This ensures that across 4/8/12 played songs, each of possible songs will be played once.
          var chunk = []; 
          if (playAnimals) {
            chunk.push(...this.animalAssets);
          }
          if (playAttributes) {
            chunk.push(...this.attributeAssets);
          }
          if (playColors) {
            chunk.push(...this.colorAssets);
          }
          toBePlayed.push(...this.shuffle(chunk));
        }

      }
      this.toBePlayed = toBePlayed;
      this.playSong();
    },
    pause() {
      console.log("Pause!");
      this.player.pause();
      this.toBePlayed = [];
      this.isPlaying = false;
    },
    intro() {
      console.log("Intro!");
      this.timeout = 20;
      this.toBePlayed = [...this.animalAssets, ...this.attributeAssets, ...this.colorAssets];
      this.playSong();
    }
  },
  created() {
    this.player.addEventListener('ended', function () {
      // switch to play button only if pause was clicked or there are no more songs in the toBePlayed list
      if (this.toBePlayed.length === 0) {
        this.isPlaying = false;
      }
      console.log("Left toBePlayed: " + this.toBePlayed.length + ", timeout: " + this.timeout);
      if (this.toBePlayed.length > 0) {
        setTimeout(function () { this.playSong() }.bind(this), this.timeout);  // 20 for intro, 2000 for play
      }
    }.bind(this));
    this.player.removeEventListener
  },
}
</script>

<style>
@font-face {
  font-family: "Caveat";
  src: local("Caveat"),
    url(./fonts/caveat.regular.ttf) format("truetype");
}

.intro_text {
  font-family: 'Caveat';
  font-size: 24px;
  line-height: 15px;
  color: white;
}

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
  height: 160px;
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
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.options {
  padding: 10px;
  margin-top: 30px;
}
</style>
