document.addEventListener("DOMContentLoaded", () => {
  let songLeft = document.getElementById("song-left");
  let songRight = document.getElementById("song-right");
  let popSong = document.querySelector(".pop-song");
  let scrollDistance = 330;

  songRight.addEventListener("click", () => {
    popSong.scrollLeft += scrollDistance;
  });

  songLeft.addEventListener("click", () => {
    popSong.scrollLeft -= scrollDistance;
  });
});
document.addEventListener("DOMContentLoaded", () => {
  let artist_left = document.getElementById("artist-left");
  let artist_right = document.getElementById("artist-right");
  let item = document.querySelector(".item");
  let scrollDistance = 330;

  artist_right.addEventListener("click", () => {
    item.scrollLeft += scrollDistance;
  });

  artist_left.addEventListener("click", () => {
    item.scrollLeft -= scrollDistance;
  });
});


const songs = [
  {
    id: 1,
    songName: `2 Number<br><div class="subtitle">Bilal Saeed</div>`,
    poster: "images/pic1.png",
    audioSrc: "audio/audio1.mp3",
  },
  {
    id: 2,
    songName: `Dope Shope  <br> <div class="subtitle"> YoYo Honey Singh</div>`,
    poster: "images/pic2.jpg",
    audioSrc: "audio/audio2.mp3",
  },
  {
    id: 3,
    songName: `Yaar Anmulle <br> <div class="subtitle"> Sharry Maan</div>`,
    poster: "images/pic3.jpeg",
    audioSrc: "audio/audio3.mp3",
  },
  {
    id: 4,
    songName: `Gabru  <br> <div class="subtitle">J Star</div>`,
    poster: "images/pic4.jpg",
    audioSrc: "audio/audio4.mp3",
  },
  {
    id: 5,
    songName: `Let Me Know <br> <div class="subtitle"> Nirvair Pannu</div>`,
    poster: "images/pic5.jpg",
    audioSrc: "audio/audio5.mp3",
  },
  {
    id: 6,
    songName: `Hass Hass  <br> <div class="subtitle">Diljit X Sia</div>`,
    poster: "images/pic6.jpg",
    audioSrc: "audio/audio6.mp3",
  },
  {
    id: 7,
    songName: `Case  <br> <div class="subtitle"> Diljit Dosanjh</div>`,
    poster: "images/pic7.jpg",
    audioSrc: "audio/audio7.mp3",
  },
  {
    id: 8,
    songName: `Satranga <br> <div class="subtitle">Arijit X Shreyas  </div>`,
    poster: "images/pic8.jpg",
    audioSrc: "audio/audio8.mp3",
  },
  {
    id: 9,
    songName: `Tujhko Jo Paaya <br> <div class="subtitle"> Mohit Chauhan</div>`,
    poster: "images/pic9.jpg",
    audioSrc: "audio/audio9.mp3",
  },
  {
    id: 10,
    songName: `Tu Hai Kahan <br> <div class="subtitle">Aur</div>`,
    poster: "images/pic10.jpg",
    audioSrc: "audio/audio10.mp3",
  },
  {
    id: 11,
    songName: `O Maahi  <br> <div class="subtitle">Arijit X Pritam</div>`,
    poster: "images/pic11.jpg",
    audioSrc: "audio/audio11.mp3",
  },
  {
    id: 12,
    songName: `Apa Fer Milaange <br> <div class="subtitle"> Savi Kahlon</div>`,
    poster: "images/pic12.jpg",
    audioSrc: "audio/audio12.mp3",
  },
  {
    id: 13,
    songName: `Locked Away  <br> <div class="subtitle">R.City[feat.Adam Levine]</div>`,
    poster: "images/pic13.jpg",
    audioSrc: "audio/audio13.mp3",
  },
  {
    id: 14,
    songName: `Peaches  <br>  <div class="subtitle"> Diljit Dosanjh</div>`,
    poster: "images/pic14.jpg",
    audioSrc: "audio/audio14.mp3",
  },
  {
    id: 15,
    songName: `Nazm Nazm <br> <div class="subtitle">Arko</div>`,
    poster: "images/pic15.jpg",
    audioSrc: "audio/audio15.mp3",
  },
  {
    id: 16,
    songName: `Dhokha Dhadi  <br>  <div class="subtitle"> Ariji Singh</div>`,
    poster: "images/pic16.jpg",
    audioSrc: "audio/audio16.mp3",
  },
  {
    id: 17,
    songName: `Lover <br>  <div class="subtitle"> Taylor Swift</div>`,
    poster: "images/pic17.png",
    audioSrc: "audio/audio17.mp3",
  },
  {
    id: 18,
    songName: `Bones <br>  <div class="subtitle">Imagine Dragons</div>`,
    poster: "images/pic18.jpg",
    audioSrc: "audio/audio18.mp3",
  },
  {
    id: 19,
    songName: `Na Na Na <br>  <div class="subtitle">Karan Aujla</div>`,
    poster: "images/pic19.jpg",
    audioSrc: "audio/audio19.mp3",
  },
  {
    id: 20,
    songName: `Jee Ni Lagda <br>  <div class="subtitle">Karan Aujla</div>`,
    poster: "images/pic20.jpg",
    audioSrc: "audio/audio20.mp3",
  },
  {
    id: 21,
    songName: `Take It Easy  <br>  <div class="subtitle">Karan Aujla & Ikky </div>`,
    poster: "images/pic21.jpg",
    audioSrc: "audio/audio21.mp3",
  },
  {
    id: 22,
    songName: `Keejo Kesari Ke Laal <br>  <div class="subtitle">Lakhbir Singh Lakha</div>`,
    poster: "images/pic22.jpg",
    audioSrc: "audio/audio22.mp3",
  },
  {
    id: 23,
    songName: `Dil Ibaadat  <br> <div class="subtitle"> KK</div>`,
    poster: "images/pic23.jpg",
    audioSrc: "audio/audio23.mp3",
  },
  {
    id: 24,
    songName: `Pehle Bhi Main <br>  <div class="subtitle"> Vishal Mishra</div>`,
    poster: "images/pic24.jpg",
    audioSrc: "audio/audio24.mp3",
  },
  {
    id: 25,
    songName: `Tere Naal  <br> <div class="subtitle">Akhil Sachdeva</div>`,
    poster: "images/pic25.jpg",
    audioSrc: "audio/audio25.mp3",
  },
  {
    id: 26,
    songName: `Love Me Like You Do <br> <div class="subtitle"> Ellie Goulding</div>`,
    poster: "images/pic26.jpg",
    audioSrc: "audio/audio26.mp3",
  },
  {
    id: 27,
    songName: `Jad Milke Baithange <br>  <div class="subtitle">Amrindar Gill</div>`,
    poster: "images/pic27.jpg",
    audioSrc: "audio/audio27.mp3",
  },
  {
    id: 28,
    songName: `Suna Suna  <br> <div class="subtitle">Shreya Ghoshal</div>`,
    poster: "images/pic28.jpg",
    audioSrc: "audio/audio28.mp3",
  },
  {
    id: 29,
    songName: `Mere Ghar Ram Aaye Hain<br> <div class="subtitle">Jubin Nautiyal</div>`,
    poster: "images/pic29.jpg",
    audioSrc: "audio/audio29.mp3",
  },
  {
    id: 30,
    songName: `Ram Aayenge  <br> <div class="subtitle"> Jaya Kishori</div>`,
    poster: "images/pic30.jpg",
    audioSrc: "audio/audio30.mp3",
  },
  {
    id: 31,
    songName: `Bindlu <br> <div class="subtitle"> Sunil Mastie </div>`,
    poster: "images/pic31.jpg",
    audioSrc: "audio/audio31.mp3",
  },
  {
    id: 32,
    songName: `Mastie MUSHUP 2020  <br>  <div class="subtitle">Sunil Mastie</div>`,
    poster: "images/pic32.jpg",
    audioSrc: "audio/audio32.mp3",
  },
  {
    id: 33,
    songName: `Sanam Teri Kasam<br>  <div class="subtitle"> Ankit Tiwari</div>`,
    poster: "images/pic33.jpeg",
    audioSrc: "audio/audio33.mp3",
  },
  {
    id: 34,
    songName: `Suna NA Sangemarmar  <br> <div class="subtitle">Arijit Singh</div>`,
    poster: "images/pic34.jpg",
    audioSrc: "audio/audio34.mp3",
  },
  {
    id: 35,
    songName: `12 Saal <br> <div class="subtitle"> Bilal Saeed</div>`,
    poster: "images/pic1.png",
    audioSrc: "audio/audio35.mp3",
  },
];

const songItems = document.getElementsByClassName("songitem");

if (songItems.length !== songs.length) {
  console.error("Array length mismatch between songItems and songs");
} else {
  Array.from(songItems).forEach((e, i) => {
    const imgElement = e.getElementsByTagName("img")[0];
    const h4Element = e.getElementsByTagName("h4")[0];

    if (imgElement && h4Element) {
      imgElement.src = songs[i].poster;
      h4Element.innerHTML = songs[i].songName;
    } else {
      console.error(`Missing img or h4 element at index ${i}`);
    }
  });
}

const music = new Audio();
let masterplay = document.getElementById("masterplay");
let wave = document.getElementById("wave"); // Ensure the ID matches your HTML
let isPaused = true; // Track the playback state
let pausedIndex = 0; // Track the index of the paused song

masterplay.addEventListener("click", () => {
  if (isPaused || music.currentTime <= 0) {
    if (isPaused) {
      music.src = songs[pausedIndex].audioSrc;
    } else {
      music.src = songs[0].audioSrc;
    }
    music.play();
    wave.classList.remove('active1');
    masterplay.classList.remove('bi-play-fill');
    masterplay.classList.add('bi-pause-fill');
    isPaused = false;
  } else {
    music.pause();
    wave.classList.add('active1');
    masterplay.classList.add('bi-play-fill');
    masterplay.classList.remove('bi-pause-fill');
    isPaused = true;
  }
});

const makeAllplays= () => {
  Array.from(document.getElementsByClassName("playlistPlay")).forEach((el) => {
        el.classList.add('bi-play-circle-fill');
        el.classList.remove('bi-pause-circle-fill');
  });
};

const makeAllBackground = () => {
  Array.from(document.getElementsByClassName("songitem")).forEach((el) => {
    el.style.backgroundColor = "rgb(105, 105, 105,.0)";
  });
};

let index = 0;
let posterplay = document.getElementById("poster-play-box");
let title = document.getElementById("title");

Array.from(document.getElementsByClassName('playlistPlay')).forEach((e) => {
  e.addEventListener("click", (el) => {
    index = parseInt(el.target.id, 10);

    if (index >= 0 && index < songs.length) {
      if (!isPaused && index === pausedIndex) {
        // If not paused and clicked the same song, toggle play/pause
        music.pause();
        makeAllBackground();
        masterplay.classList.add('bi-play-fill');
        masterplay.classList.remove('bi-pause-fill');
        isPaused = true;
      } else {
        // Change to a new song
        music.src = songs[index].audioSrc;
        music.play();
        masterplay.classList.remove('bi-play-fill');
        masterplay.classList.add('bi-pause-fill');
        makeAllBackground();
        makeAllplays();
        el.target.classList.add('bi-pause-circle-fill');
        el.target.classList.remove('bi-play-circle-fill');
        Array.from(document.getElementsByClassName("songitem"))[index].style.backgroundColor = "rgb(105, 105, 105,.1)";
        // Update the poster image
        posterplay.src = songs[index].poster;
        // Update the song title
        title.innerHTML = songs[index].songName;
        isPaused = false;
        pausedIndex = index;
      }
    } else {
      console.error(`Invalid index: ${index}`);
    }
  });
});


  let currentstart = document.getElementById("currentstart");
  let currentEnd = document.getElementById("currentEnd");
  let seek = document.getElementById("seek");
  let bar2 = document.getElementById("bar2");
  let dot = document.getElementsByClassName("dot")[0];
  music.addEventListener("timeupdate", () => {
    let musiccur = music.currentTime;
    let musicdur = music.duration;

    let min1 = Math.floor(musicdur / 60);
    let sec1 = Math.floor(musicdur % 60);

    if (sec1 < 10) {
      sec1 = `0${sec1}`;
    }
    currentEnd.innerText = `${min1}:${sec1}`;

    let min2 = Math.floor(musiccur / 60);
    let sec2 = Math.floor(musiccur % 60);
    if (sec2 < 10) {
      sec2 = `0${sec2}`;
    }
    currentstart.innerText = `${min2}:${sec2}`;

    let progressbar = parseInt((musiccur / musicdur)*100);
    seek.value = progressbar;
    // console.log(seek.value);
    let seekbar= seek.value;
    bar2.style.width=  `${seekbar}%`;
    dot.style.left= `${seekbar}%`;
  });

seek.addEventListener("change",()=>{
  music.currentTime=seek.value * music.duration / 100;
});



let volicon = document.getElementById("vol-icon");
let vol = document.getElementById("vol");
let volbar = document.getElementsByClassName("vol-bar")[0];
let voldot = document.getElementById("vol-dot");

vol.addEventListener('change', () => {
  if (vol.value == 0) {
    volicon.classList.remove("bi-volume-up-fill");
    volicon.classList.remove("bi-volume-down-fill");
    volicon.classList.add("bi-volume-mute-fill");
  }
  if (vol.value > 0) {
    volicon.classList.remove("bi-volume-up-fill");
    volicon.classList.add("bi-volume-down-fill");
    volicon.classList.remove("bi-volume-mute-fill");
  }
  if (vol.value > 50) {
    volicon.classList.add("bi-volume-up-fill");
    volicon.classList.remove("bi-volume-down-fill");
    volicon.classList.remove("bi-volume-mute-fill");
  }
  
  let vola = parseFloat(vol.value); 
  volbar.style.width = `${vola}%`;
  voldot.style.left = `${vola}%`;
  music.volume = vola / 100;
});

let back=document.getElementById("back");
let next= document.getElementById("next");

back.addEventListener('click', () => {
  index -= 1;
  if (index < 0) {
    index = songs.length - 1; // If at the beginning, go to the last song
  }
  if (music.currentTime <= 0) {
    // If already at the beginning, start from the end
    music.src = songs[index].audioSrc;
    music.play();
    masterplay.classList.remove('bi-play-fill');
    masterplay.classList.add('bi-pause-fill');
    makeAllBackground();
    makeAllplays();
    document.getElementById(index).classList.add('bi-pause-circle-fill');
    document.getElementById(index).classList.remove('bi-play-circle-fill');
    Array.from(document.getElementsByClassName("songitem"))[index].style.backgroundColor = "rgb(105, 105, 105,.1)";
    // Update the poster image
    posterplay.src = songs[index].poster;
    // Update the song title
    title.innerHTML = songs[index].songName;
    isPaused = false;
    pausedIndex = index;
  } else {
    music.src = songs[index].audioSrc;
    music.play();
    masterplay.classList.remove('bi-play-fill');
    masterplay.classList.add('bi-pause-fill');
    makeAllBackground();
    makeAllplays();
    document.getElementById(index).classList.add('bi-pause-circle-fill');
    document.getElementById(index).classList.remove('bi-play-circle-fill');
    Array.from(document.getElementsByClassName("songitem"))[index].style.backgroundColor = "rgb(105, 105, 105,.1)";
    // Update the poster image
    posterplay.src = songs[index].poster;
    // Update the song title
    title.innerHTML = songs[index].songName;
    isPaused = false;
    pausedIndex = index;
  }
});

next.addEventListener('click', () => {
  index += 1;
  if (index >= songs.length) {
    index = 0; // If at the end, go to the first song
  }
  if (music.currentTime >= music.duration) {
    // If already at the end, start from the beginning
    music.src = songs[index].audioSrc;
    music.play();
    masterplay.classList.remove('bi-play-fill');
    masterplay.classList.add('bi-pause-fill');
    makeAllBackground();
    makeAllplays();
    document.getElementById(index).classList.add('bi-pause-circle-fill');
    document.getElementById(index).classList.remove('bi-play-circle-fill');
    Array.from(document.getElementsByClassName("songitem"))[index].style.backgroundColor = "rgb(105, 105, 105,.1)";
    // Update the poster image
    posterplay.src = songs[index].poster;
    // Update the song title
    title.innerHTML = songs[index].songName;
    isPaused = false;
    pausedIndex = index;
  } else {
    music.src = songs[index].audioSrc;
    music.play();
    masterplay.classList.remove('bi-play-fill');
    masterplay.classList.add('bi-pause-fill');
    makeAllBackground();
    makeAllplays();
    document.getElementById(index).classList.add('bi-pause-circle-fill');
    document.getElementById(index).classList.remove('bi-play-circle-fill');
    Array.from(document.getElementsByClassName("songitem"))[index].style.backgroundColor = "rgb(105, 105, 105,.1)";
    // Update the poster image
    posterplay.src = songs[index].poster;
    // Update the song title
    title.innerHTML = songs[index].songName;
    isPaused = false;
    pausedIndex = index;
  }
});

let searchInput = document.getElementById("searchInput");
let searchIcon = document.getElementById("searchIcon");

searchIcon.addEventListener("click", () => {
    search();
});

searchInput.addEventListener("keypress", (e) => {
    if (e.key === "Enter") {
        search();
    }
});

