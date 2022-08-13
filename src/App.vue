<template>
  <div id="app">
    <header>
      <h1>Sounds Great</h1>
    </header>
    <main>
      <section class="options">
        <div class="options">
          <input type="checkbox" id="animal" name="animal" checked>
          <label for="animal">🐷<!-- animal --></label><!-- <br>  -->
          <input type="checkbox" id="attribute" name="attribute">
          <label for="attribute">👕<!-- attribute --></label><!-- <br>  -->
          <input type="checkbox" id="color" name="color">
          <label for="color">🌈<!-- color --></label><!-- <br>  -->
        </div>
      </section>
      <br>
      <section class="player">
        <h2 class="song-title">{{ current.title }}</h2>
        <div class="control">
          <button class="play" v-if="!isPlaying" @click="play"> ▶️ </button>
          <button class="pause" v-else @click="pause"> ⏸ </button>
          <button class="intro" @click="intro"> ♻ </button>
        </div>
      </section>
      <br>
      <section class="playlist">
        <!-- <h3>Animals</h3> -->
        <button v-for="song in animalAssets" :key="song.sound" @click="playSong(song)" :class="(song.sound == current.sound) ? 'song playing' : 'song'">
          {{ song.image }}
        </button>
        <br>
        <!-- <h3>Attributes</h3> -->
        <button v-for="song in attributeAssets" :key="song.sound" @click="playSong(song)" :class="(song.sound == current.sound) ? 'song playing' : 'song'">
          {{ song.image }}
        </button>
        <br>
        <!-- <h3>Colors</h3> -->
        <button v-for="song in colorAssets" :key="song.sound" @click="playSong(song)" :class="(song.sound == current.sound) ? 'song playing' : 'song'">
          {{ song.image }}
        </button>
      </section>
    </main>
  </div>
</template>

<script>

export default {
  name: 'app',
  data () {
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
          image: '🐈',
        },
        {
          title: 'cow',
          sound: require('./assets/animals/cow.mp3'),
          image: '🐄',
        },
        {
          title: 'elephant',
          sound: require('./assets/animals/elephant.mp3'),
          image: '🐘',
        },
        {
          title: 'snake',
          sound: require('./assets/animals/snake.mp3'),
          image: '🐍',
        },
      ],
      attributeAssets: [
        {
          title: 'boots',
          sound: require('./assets/attributes/boots.mp3'),
          image: '👟',
        },
        {
          title: 'glasses',
          sound: require('./assets/attributes/glasses.mp3'),
          image: '👓',
        },
        {
          title: 'hat',
          sound: require('./assets/attributes/hat.mp3'),
          image: '👒',
        },
        {
          title: 'umbrella',
          sound: require('./assets/attributes/umbrella.mp3'),
          image: '☔',
        },
      ],
      colorAssets: [
        {
          title: 'blue',
          sound: require('./assets/colors/blue.mp3'),
          image: '🟦',
        },
        {
          title: 'green',
          sound: require('./assets/colors/green.mp3'),
          image: '🟩',
        },
        {
          title: 'red',
          sound: require('./assets/colors/red.mp3'),
          image: '🟥',
        },
        {
          title: 'yellow',
          sound: require('./assets/colors/yellow.mp3'),
          image: '🟨',
        },
      ],
      player: new Audio()
    }
  },
  methods: {
    getRandom (array) {
      return array[Math.floor(Math.random() * array.length)];
    },
    playSong (song) {
      this.current = this.toBePlayed.shift();
      this.player.src = this.current.sound;

      if (song != undefined && song.sound != undefined) {
        this.current = song;
        this.player.src = this.current.sound;
      }
      console.log(this.current.title);
      this.player.play();
      this.isPlaying = true;
    },
    play () {
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
    pause () {
      this.player.pause();
      this.isPlaying = false;
    },
    intro () {
      this.toBePlayed = [...this.animalAssets, ...this.attributeAssets, ...this.colorAssets];
      this.playSong();
    }
  },
  created() {
    
    this.player.addEventListener('ended', function () {
      this.isPlaying = false;
      console.log(this.toBePlayed.length);
      if (this.toBePlayed.length > 0) {
        setTimeout(function(){ this.playSong() }.bind(this), 10);  // 2000
      }
    }.bind(this));
  }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
body {
  font-family: sans-serif;
}
header {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 15px;
  background-color: #212121;
  color: #FFF;
}
main {
  width: 100%;
  max-width: 768px;
  margin: 0 auto;
}
</style>
