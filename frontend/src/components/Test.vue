<template>
    <div>
        <div class="header">
        <router-link class="backB"
          :to="{name: 'dictionary', params: {name:this.categoryName}}"
              ><button >=</button></router-link>
        <h1>Test task</h1>
      </div> 
      <h4>{{ numberOfQuestions }}/10</h4>
      <div id="question">
        <h2>{{ currantlyWord.word }}</h2>
        <div class="options">
          <button 
            :id="'answer-option-' + currantlyWord.translate0"
            class="default-option"
            @click="selectOption(currantlyWord.translate0)"
          >{{ currantlyWord.translate0 }}</button>
          <button 
            :id="'answer-option-' + currantlyWord.translate1"
            @click="selectOption(currantlyWord.translate1)"
            class="default-option"
            >{{ currantlyWord.translate1 }}</button>
          <button 
            :id="'answer-option-' + currantlyWord.translate2"
            @click="selectOption(currantlyWord.translate2)"
            class="default-option"
            >{{ currantlyWord.translate2 }}</button>
          <button 
            :id="'answer-option-' + currantlyWord.translate3"
            @click="selectOption(currantlyWord.translate3)"
            class="default-option"
            >{{ currantlyWord.translate3 }}</button>
          </div>
      </div>
      <h2>{{ categoryName }}</h2>
      <button @click="nextTest()">next</button>
    </div>
  </template>
  
  <script>
  export default{
    data(){
        return {
            currantlyWord:{},
            score: 0,
            failing:0,
            numberOfQuestions: 0
        }
    },
    props: {
      categoryName: {
        type:[String],
        required: true
      }
    },
    methods:{
      defaultOptionStyle(){
        var element = document.getElementById('answer-option-' + this.currantlyWord.translate0);
          element.style.backgroundColor = 'azure';
          element = document.getElementById('answer-option-' + this.currantlyWord.translate1);
          element.style.backgroundColor = 'azure';
          element = document.getElementById('answer-option-' + this.currantlyWord.translate2);
          element.style.backgroundColor = 'azure';
          element = document.getElementById('answer-option-' + this.currantlyWord.translate3);
          element.style.backgroundColor = 'azure';
      },
      dissabledButtons(value){
        var element = document.getElementById('answer-option-' + this.currantlyWord.translate0);
          element.disabled=value;
          element.classList.add('default-option');
          element = document.getElementById('answer-option-' + this.currantlyWord.translate1);
          element.disabled=value;
          element = document.getElementById('answer-option-' + this.currantlyWord.translate2);
          element.disabled=value;
          element = document.getElementById('answer-option-' + this.currantlyWord.translate3);
          element.disabled=value;
      },
      nextTest() {
        if(this.numberOfQuestions!=3){
          this.getWordData();
          this.dissabledButtons(false);
          this.defaultOptionStyle();
        }
        else{
          this.$router.push({
              name: 'result',
              params: { categoryName: this.categoryName }
          });
          
        }
      },
      selectOption(selected_translate){
        fetch(`http://localhost:8000/is_true_translate/${this.categoryName}/${this.currantlyWord.word}/${selected_translate}`,{
              method:'GET',
              headers: {"Content-Type":"application/json"}
          })
          .then(resp=>resp.json())
          .then(data=>{
              if(data==true){
                var element = document.getElementById('answer-option-' + selected_translate);
                element.style.backgroundColor = 'lightgreen';
                this.score+=1;
                this.numberOfQuestions+=1;
              }
              else{
                var element = document.getElementById('answer-option-' + selected_translate);
                element.style.backgroundColor = 'lightpink'; 
                this.failing+=1;
                this.numberOfQuestions+=1;   
              }
              this.dissabledButtons(true);
          })
          .catch(error=>{console.log(error)})

          
      },
        getWordData() {
          fetch(`http://localhost:8000/fourWords/${this.categoryName}`,{
              method:'GET',
              headers: {"Content-Type":"application/json"}
          })
          .then(resp=>resp.json())
          .then(data=>{
              this.currantlyWord = data
          })
          .catch(error=>{console.log(error)})
      }
    },
    created() {
      this.getWordData()
    }
  }
  </script>
  
<style>
#question{
  text-align: center;
}
.options{
  display: grid;
  grid-template-columns: 1fr 1fr;
}
.default-option{
  padding: 15px;
  font-size: 15px;
  color: black;
  border-width: 2px;
  border-style: solid;
  border-color: blueviolet;
  background-color: azure;
}
</style>