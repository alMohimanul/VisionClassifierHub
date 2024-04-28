<template>
  <v-app id="inspire">
    <v-navigation-drawer v-model="drawer" color="black">
      <v-sheet
        class="pa-4"
        style="background-color: black;"
      >
        <div class="logo">
          <h1>VisionClassifierHub</h1>
        </div>
      </v-sheet>

      <v-divider>
        
      </v-divider>

<v-list>
  <v-list-item
    v-for="[text] in links"
    :key="text"
    link
    class="text-center pa-4"
    @click="selectButton(text)"
  >
  <!-- style="font-size: 14px; text-transform: none; white-space: normal; min-width: 100px;" -->
    <v-btn
     block=true
     :color="selectedButton === text ? 'blue' : 'black'"
     lowercase=true
     class="mx-auto pa-8"
     style="
     text-transform: none;
     font-family:Arial, Helvetica, sans-serif !important;
     font-size: 16px; white-space: normal;
     border-radius: 30px;
     text-align: left; "
    >
      {{ text }}
    </v-btn>
    <v-list-item-content>
      <v-row>
        <v-col cols="auto">
          <v-list-item-title></v-list-item-title>
        </v-col>
      </v-row>
    </v-list-item-content>
  </v-list-item>
</v-list>




    </v-navigation-drawer>

    <v-main>
      <v-container
        class="py-8 px-6 ml-16"
        fluid
      >
        <v-row>
          <v-col
            v-for="card in card1"
            :key="card"
            cols="12"
          >
  <v-card>
  <span v-if="selectedButton === 'Plants Classification' || selectedButton === 'Polyp Segmentation' || selectedButton === 'Lung Tumor Detection' "
   style=" opacity: 0.7;
   color: #888;
   font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
   white-space: nowrap;
   font-size: 18px;
   margin-left:12%;">
   *This is for educational purposes only and should not be used as a substitute for professional medical advice.
  </span>
   <span v-else-if="selectedButton === 'Wildfire Classification'"
   style=" opacity: 0.7;
   color: #888;
   font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
   white-space: nowrap;
   font-size: 18px;
   margin-left:13%;">
   *This is for educational purposes only and should not be used as a substitute for professional climate advice.
  </span>
  <v-list style="box-shadow: 0 10px 4px rgba(0, 0, 0, 0.1);" lines="two">
    <v-list-subheader :title="card1"></v-list-subheader>
    <div v-if="selectedButton === 'Plants Classification'">
       <div class="photo-box" v-if="!plantImageUrl" @click="choosePhoto">
    <span class="add-photo-text">+ Add photo to classify</span>
    <input type="file" accept="image/*" class="file-input" id="file-input" style="display: none;" @change="handleFileChange">
  </div>
  <div v-else class="photo-box">
    <img :src="plantImageUrl" alt="Selected Photo" class="photo" style="width: 100%; height: 100%;">
  </div>
  <button v-if="!plantImageUrl" class="custom-button" @click="choosePhoto">Select Photo</button>
  <button v-else-if="processed" class="process-button custom-button" @click="tryAgain">Try Again</button>
  <button v-else class="process-button custom-button" @click="processPhoto">Process</button>
  </div>

  <div v-else-if="selectedButton === 'Wildfire Classification'">
      <div class="photo-box" v-if="!wildfireImageUrl" @click="choosePhoto">
    <span class="add-photo-text">+ Add photo to classify</span>
    <input type="file" accept="image/*" class="file-input" id="file-input" style="display: none;" @change="handleFileChange">
  </div>
  <div v-else class="photo-box">
    <img :src="wildfireImageUrl" alt="Selected Photo" class="photo" style="width: 100%; height: 100%;">
  </div>
  <button v-if="!wildfireImageUrl" class="custom-button" @click="choosePhoto">Select Photo</button>
  <button v-else-if="processed" class="process-button custom-button" @click="tryAgain">Try Again</button>
  <button v-else class="process-button custom-button" @click="processPhoto">Process</button>
  </div>


  <div v-else-if="selectedButton === 'Polyp Segmentation'">
      <div class="photo-box" v-if="!polypImageUrl" @click="choosePhoto">
    <span class="add-photo-text">+ Add photo to classify</span>
    <input type="file" accept="image/*" class="file-input" id="file-input" style="display: none;" @change="handleFileChange">
  </div>
  <div v-else class="photo-box">
    <img :src="polypImageUrl" alt="Selected Photo" class="photo" style="width: 100%; height: 100%;">
  </div>
  <button v-if="!polypImageUrl" class="custom-button" @click="choosePhoto">Select Photo</button>
  <button v-else-if="processed" class="process-button custom-button" @click="tryAgain">Try Again</button>
  <button v-else class="process-button custom-button" @click="processPhoto">Process</button>
  </div>

  <div v-else-if="selectedButton === 'Lung Tumor Detection'">
      <div class="photo-box" v-if="!lungImageUrl" @click="choosePhoto">
    <span class="add-photo-text">+ Add photo to classify</span>
    <input type="file" accept="image/*" class="file-input" id="file-input" style="display: none;" @change="handleFileChange">
  </div>
  <div v-else class="photo-box">
    <img :src="lungImageUrl" alt="Selected Photo" class="photo" style="width: 100%; height: 100%;">
  </div>
  <button v-if="!lungImageUrl" class="custom-button" @click="choosePhoto">Select Photo</button>
  <button v-else-if="processed" class="process-button custom-button" @click="tryAgain">Try Again</button>
  <button v-else class="process-button custom-button" @click="processPhoto">Process</button>
  </div>
  
  </v-list>
</v-card>

          </v-col>

              <v-col
            v-for="card in card2"
            :key="card"
            cols="12"
          >
  <v-card>
  <v-list style="background-color: grey; display: flex; align-items: center;" lines="two">
    <v-list-subheader :title="card1"></v-list-subheader>
     <span style="color: white; font-size: 22px; font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin-left:19%;">
      Class Name: {{ responsedClass }}
      </span>
       <span style="color: white; font-size: 22px; font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin-left:18%;">
      Confidence Score: {{ respondedScore }}
      </span>
  </v-list>
</v-card>

          </v-col>




        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script setup>
  import { ref } from 'vue'

  const card1 = ['']
  const card2 = ['']

  const links = [
    ['Plants Classification'],
    ['Wildfire Classification'],
    ['Polyp Segmentation'],
    ['Lung Tumor Detection'],
  ];

  const drawer = ref(null)
</script>

<script>
import axios from 'axios';
  export default {
    data: () => ({
      cards: ['Today'],
      drawer: null,
      red: 'blue',
      selectedButton: 'Plants Classification',
      plantImageUrl: null,
      wildfireImageUrl: null,
      polypImageUrl: null,
      lungImageUrl: null,
      showProcessButton: false,
      fileInput: null,
      responsedClass: null,
      respondedScore: null,
      processed: false,
    }),

     methods: {
      choosePhoto() {
        // Simulate click event on the file input element
        document.getElementById('file-input').click();
      },
      tryAgain() {
        this.plantImageUrl = '';
        this.processed = false;
        this.responsedClass = '';
        this.respondedScore = '';
      },
     async handleFileChange(event) {
      const file = event.target.files[0];
      this.fileInput = file;
      // console.log('Selected file:', file);
    
      if (file) {
        if (this.selectedButton === 'Plants Classification') {
             this.plantImageUrl = URL.createObjectURL(file);
             this.wildfireImageUrl = null;
             this.polypImageUrl = null;
             this.lungImageUrl = null;
         } else if (this.selectedButton === 'Wildfire Classification') {
             this.wildfireImageUrl = URL.createObjectURL(file);
             this.plantImageUrl = null;
             this.polypImageUrl = null;
             this.lungImageUrl = null;
        } else if (this.selectedButton === 'Polyp Segmentation') {
             this.polypImageUrl = URL.createObjectURL(file);
             this.wildfireImageUrl = null;
             this.plantImageUrl = null;
             this.lungImageUrl = null;
        } else if (this.selectedButton === 'Lung Tumor Detection') {
             this.lungImageUrl = URL.createObjectURL(file);
              this.wildfireImageUrl = null;
              this.plantImageUrl = null;
              this.polypImageUrl = null;
        }
        this.showProcessButton = true; 
      }
    },
    async processPhoto(){
      const formData = new FormData();
      formData.append('file', this.fileInput);
      console.log('Form data:', formData);
      try {
        const response = await axios.post('http://localhost:8000/predict', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });
        // console.log('Prediction class:', response.data.class);
        this.responsedClass = response.data.class;
        this.respondedScore = response.data.confidence.toFixed(2);
        this.processed = true;
      } catch (error) {
        console.error('Error uploading image:', error);
      }
    },
     selectButton(buttonText) {
      this.selectedButton = buttonText;
    },
    }
    
  }
</script>
