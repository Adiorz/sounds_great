<template>
  <div id="app">
    <div class="player">
      <div class="options">
        <div class="option">
          <input type="checkbox" id="animal" name="animal" checked>
          <label for="animal" class="icon"><img :src="iconAssets.animal" class="icon_img" /></label>
        </div>
        <br>
        <div class="option">
          <input type="checkbox" id="instrument" name="instrument">
          <label for="instrument" class="icon"><img :src="iconAssets.instrument" class="icon_img" /></label>
        </div>
        <br>
        <div class="option">
          <input type="checkbox" id="color" name="color">
          <label for="color" class="icon"><img :src="iconAssets.color" class="icon_img" /></label>
        </div>
      </div>
      <div class="control">
        <button class="play" v-if="!isPlaying" @click="play">
          <svg class="play_img" viewBox="0 0 280 280" xmlns="http://www.w3.org/2000/svg" version="1.1"
            xml:space="preserve">
            <g>
              <path
                d="m280,25c0,-13.807 -11.193,-25 -25,-25l-230,0c-13.807,0 -25,11.193 -25,25l0,230c0,13.807 11.193,25 25,25l230,0c13.807,0 25,-11.193 25,-25l0,-230zm-91.153,127.047l-79.192,51.693c-10.123,6.629 -18.655,2.152 -18.655,-9.948l0,-107.584c0,-12.1 8.532,-16.577 18.656,-9.949l79.066,51.685c10.123,6.628 10.248,17.474 0.125,24.103z"
                fill="#7fb762" data-original="#000000" id="svg_2" xmlns="http://www.w3.org/2000/svg" />
              <text transform="matrix(7.90178 0 0 5.50952 -620.323 -624.598)" stroke="#000" xml:space="preserve"
                text-anchor="start" font-family="'Caveat'" font-size="8" id="svg_2" y="159.07375" x="99.14896"
                stroke-width="0" fill="white">play</text>
            </g>
          </svg>
        </button>
        <button class="pause" v-else @click="pause">
          <svg class="pause_img" viewBox="0 0 280 280" xmlns="http://www.w3.org/2000/svg" xml:space="preserve"
            version="1.1">
            <g>
              <path id="svg_2" data-original="#000000" fill="#ea394e"
                d="m280,25c0,-13.807 -11.193,-25 -25,-25l-230,0c-13.807,0 -25,11.193 -25,25l0,230c0,13.807 11.193,25 25,25l230,0c13.807,0 25,-11.193 25,-25l0,-230zm-159,168.439c0,10.217 -8.282,18.5 -18.5,18.5c-10.218,0 -18.5,-8.283 -18.5,-18.5l0,-106.878c0,-10.217 8.282,-18.5 18.5,-18.5c10.218,0 18.5,8.283 18.5,18.5l0,106.878zm75,0c0,10.217 -8.282,18.5 -18.5,18.5c-10.218,0 -18.5,-8.283 -18.5,-18.5l0,-106.878c0,-10.217 8.282,-18.5 18.5,-18.5c10.218,0 18.5,8.283 18.5,18.5l0,106.878z"
                xmlns="http://www.w3.org/2000/svg" />
              <text transform="matrix(7.90178 0 0 5.50952 -620.323 -624.598)" stroke="#000" xml:space="preserve"
                text-anchor="start" font-family="'Caveat'" font-size="8" id="svg_2" y="159.07375" x="97.14896"
                stroke-width="0" fill="white">pause</text>
            </g>
          </svg>
        </button><br>
        <button class="intro" @click="intro">
          <div><img :src="iconAssets.intro" class="intro_img" /></div>
          <div><text class="intro_text" style="font-family='Caveat'">intro</text></div>
        </button>
      </div>
    </div>
    <div class="playlist">
      <!-- TODO: base on playing sound, modicy border color of icon/image -->
      <div class='demo_buttons'>
        <button v-for="song in animalAssets" :key="song.sound" @click="playSong(song)"
          :class="[song.title + '_icon', 'icon']">
          <img :src="song.image" class="icon_img" />
        </button>
      </div>
      <div class='demo_buttons'>
        <button v-for="song in instrumentAssets" :key="song.sound" @click="playSong(song)"
          :class="[song.title + '_icon', 'icon']">
          <img :src="song.image" class="icon_img" />
        </button>
      </div>
      <div class='demo_buttons'>
        <button v-for="song in colorAssets" :key="song.sound" @click="playSong(song)"
          :class="[song.title + '_icon', 'icon']">
          <img :src="song.image" class="icon_img" />
        </button>
      </div>
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
      colorsSelected: false,  // this should hold the value
      iconAssets: {
        "intro": require('./assets/icons/intro.svg'),
        "animal": require('./assets/options/animal.svg'),
        "instrument": require('./assets/options/instrument.svg'),
        "color": require('./assets/options/color.svg'),
      },
      animalAssets: [
        {
          title: 'cat',
          sound: require('./assets/animals/cat.mp3'),
          image: require('./assets/animals/cat.svg'),
        },
        {
          title: 'cow',
          sound: require('./assets/animals/cow.mp3'),
          image: require('./assets/animals/cow.svg'),
        },
        {
          title: 'elephant',
          sound: require('./assets/animals/dog.mp3'),
          image: require('./assets/animals/dog.svg'),
        },
        {
          title: 'snake',
          sound: require('./assets/animals/duck.mp3'),
          image: require('./assets/animals/duck.svg'),
        },
      ],
      instrumentAssets: [
        {
          title: 'drum',
          sound: require('./assets/instruments/drum.mp3'),
          image: require('./assets/instruments/drum.svg'),
        },
        {
          title: 'guitar',
          sound: require('./assets/instruments/guitar.mp3'),
          image: require('./assets/instruments/guitar.svg'),
        },
        {
          title: 'piano',
          sound: require('./assets/instruments/piano.mp3'),
          image: require('./assets/instruments/piano.svg'),
        },
        {
          title: 'saxophone',
          sound: require('./assets/instruments/saxophone.mp3'),
          image: require('./assets/instruments/saxophone.svg'),
        },
      ],
      colorAssets: [
        {
          title: 'blue',
          sound: require('./assets/colors/blue.mp3'),
          image: require('./assets/colors/blue.svg'),
        },
        {
          title: 'green',
          sound: require('./assets/colors/green.mp3'),
          image: require('./assets/colors/green.svg'),
        },
        {
          title: 'red',
          sound: require('./assets/colors/red.mp3'),
          image: require('./assets/colors/red.svg'),
        },
        {
          title: 'yellow',
          sound: require('./assets/colors/yellow.mp3'),
          image: require('./assets/colors/yellow.svg'),
        },
      ],
      player: new Audio(),
    }
  },
  methods: {
    colorsChangeSelected() {
      this.colorsSelected = !this.colorsSelected;
    },
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
    shouldPlayAnimals() {
      return document.querySelector('#animal').checked;
    },
    shouldPlayinstruments() {
      return document.querySelector('#instrument').checked;
    },
    shouldPlayColors() {
      return document.querySelector('#color').checked;
    },
    getToBePlayedChunk() {
      // Get chunk of toBePlayed tpiano contains all possible items selected. 
      var chunk = [];
      if (this.shouldPlayAnimals()) {
        chunk.push(...this.animalAssets);
      }
      if (this.shouldPlayinstruments()) {
        chunk.push(...this.instrumentAssets);
      }
      if (this.shouldPlayColors()) {
        chunk.push(...this.colorAssets);
      }
      return chunk;
    },
    play() {
      console.log("Play!");
      this.timeout = 2000;
      var toBePlayed = [];
      if (this.toBePlayed.length === 0) { // do not add new songs for multiple play buttons
        for (let i = 0; i < 100; i++) {
          // Using toBePlayedChunks ensures tpiano across 4/8/12 played songs, each of possible songs will be played once.
          toBePlayed.push(...this.shuffle(this.getToBePlayedChunk()));
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
      this.timeout = 1000;
      this.toBePlayed = this.getToBePlayedChunk();
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
        // 20 for intro, 2000 for play
        setTimeout(function () { this.playSong() }.bind(this), this.timeout);
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

input {
  accent-color: #4b98d4;
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

.icon_img {
  max-width: 50px;
  max-height: 50px;
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
}

.pause_img {
  margin: 25px 0 0 0;
  width: 160px;
  height: 160px;
}

.intro {
  margin: -50px 0 10px 0;
  width: 160px;
  height: 40px;
  border: 0;
  background: #4b98d4;
  border-radius: 5%;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.options {
  padding: 10px;
  margin-top: 30px;
}

.demo_buttons {
  border-color: transparent;
  border-width: 1px;
  border-style: dotted;
}

</style>
