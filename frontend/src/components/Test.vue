<template>
    <div>
        <div class="header">
        <router-link class="backB"
          :to="{name: 'dictionary', params: {name:this.categoryName}}"
              ><button >=</button></router-link>
        <h1>Test task</h1>
      </div> 
      <h4>{{ currantlyIndex+1 }}/10</h4>
      <div id="question">
        <h2>{{ test[currantlyIndex].word }}</h2>
        <div class="options">
          <button 
            id="option1"
            class="default-option"
            @click="selectOption('option1', test[currantlyIndex].option1 )"
          >{{ test[currantlyIndex].option1 }}</button>
          <button 
            id="option2"
            @click="selectOption('option2', test[currantlyIndex].option2)"
            class="default-option"
            >{{ test[currantlyIndex].option2 }}</button>
          <button 
            id="option3"
            @click="selectOption('option3', test[currantlyIndex].option3)"
            class="default-option"
            >{{ test[currantlyIndex].option3 }}</button>
          <button 
            id="option4"
            @click="selectOption('option4', test[currantlyIndex].option4)"
            class="default-option"
            >{{ test[currantlyIndex].option4 }}</button>
          </div>
      </div>
      <button @click="nextTest()">next</button>
    </div>
  </template>
  
  <script>
  export default{
    data(){
        return {
            test:[],
            currantlyIndex: 0,
            
        }
    },
    props: {
      categoryName: {
        type:[String],
        required: true
      }
    },
    methods:{
      removeFocus(){
        const focusedElements = document.querySelectorAll(':focus');
        focusedElements.forEach(element => {
          element.blur();
        });
      },
      nextTest() {
        if(this.currantlyIndex!=9){
          fetch(`http://localhost:8000/check_word/${this.categoryName}`,{
              method:'POST',
              headers: {"Content-Type":"application/json"},
              body: JSON.stringify({
                word: this.test[this.currantlyIndex].word,
                answer: this.test[this.currantlyIndex].answer,
                option1: this.test[this.currantlyIndex].option1,
                option2: this.test[this.currantlyIndex].option2,
                option3: this.test[this.currantlyIndex].option3,
                option4: this.test[this.currantlyIndex].option4 
              })
          })
          .then(resp=>resp.json())
            .then(data=>{
              
              this.removeFocus();
              
              console.log(data)
              // if(data==true){
                
              // }
              // else if(data==false){
                
              // }
              console.log(data)
            })
            .catch(error=>{console.log(error)})

          this.currantlyIndex+=1
        }
        else {
          this.getScore()
        }
      },
      selectOption(id, selected_translate){
        this.test[this.currantlyIndex].answer=selected_translate
        var element = document.getElementById(id)
        console.log(selected_translate)
          console.log(id)
        // this.test[this.currantlyIndex].answer=element;
        element.focus();
      },
      getScore(){
        fetch(`http://localhost:8000/check_result/${this.categoryName}`,{
              method:'POST',
              headers: {"Content-Type":"application/json"},
              body: JSON.stringify({questions: this.test})
          })
          .then(resp=>resp.json())
            .then(data=>{
            console.log(data)
            })
            .catch(error=>{console.log(error)})
      },
      getWordData() {
          fetch(`http://localhost:8000/getTest/${this.categoryName}`,{
              method:'GET',
              headers: {"Content-Type":"application/json"}
          })
          .then(resp=>resp.json())
          .then(data=>{
            this.test.push(...data)
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
.default-option:focus{
  background-color: skyblue;
}
</style>