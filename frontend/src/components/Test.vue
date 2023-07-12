<template>
    <div>
        <div class="header">
        <router-link class="backB"
          :to="{name: 'dictionary', params: {name:this.categoryName}}"
              ><button >=</button></router-link>
        <h1>Test task</h1>
      </div> 
      <div id="question">
      <h4>{{ currantlyIndex+1 }}/10</h4>
      <div id="wordAndOptions">
        <h2>{{ test[currantlyIndex].word }}</h2>
        <div class="options">
          <button 
            id="option1"
            :class="{'defaultB': option1_x===0, 'trueAnswer': option1_x===true, 'falseAnswer': option1_x===false}"
            @click="selectOption('option1', test[currantlyIndex].option1 )"
          >{{ test[currantlyIndex].option1 }}</button>
          <button 
            id="option2"
            @click="selectOption('option2', test[currantlyIndex].option2)"
            :class="{'defaultB': option2_x===0, 'trueAnswer': option2_x===true, 'falseAnswer': option2_x===false}"
            >{{ test[currantlyIndex].option2 }}</button>
          <button 
            id="option3"
            @click="selectOption('option3', test[currantlyIndex].option3)"
            :class="{'defaultB': option3_x===0, 'trueAnswer': option3_x===true, 'falseAnswer': option3_x===false}"
            >{{ test[currantlyIndex].option3 }}</button>
          <button 
            id="option4"
            @click="selectOption('option4', test[currantlyIndex].option4)"
            :class="{'defaultB': option4_x===0, 'trueAnswer': option4_x===true, 'falseAnswer': option4_x===false}"
            >{{ test[currantlyIndex].option4 }}</button>
          </div>
      </div>
      <button 
        id="next"
        @click="nextTest()"
        >next</button>
      </div>
        <div id="results">
          <h2>Правильні відповіді: {{ results.score }}/{{ results.size }}</h2>
          <h2>Помилки: {{ results.faile }}</h2>
          <h2>Пропущено: {{ results.passed }}</h2>
          <h2>Точність: {{ results.precision*100 }}%</h2>
        </div>
    </div>
  </template>
  
  <script>
  export default{
    data(){
        return {
            test:[],
            currantlyIndex: 0,
            results:{},
            option1_x: 0,
            option2_x: 0,
            option3_x: 0,
            option4_x: 0
        }
    },
    props: {
      categoryName: {
        type:[String],
        required: true
      }
    },
    methods:{
      disabledAllButtons(value){
        var element = document.getElementById('option1')
        element.disabled = value;
        element = document.getElementById('option2')
        element.disabled = value;
        element = document.getElementById('option3')
        element.disabled = value;
        element = document.getElementById('option4')
        element.disabled = value;
        element = document.getElementById('next')
        element.disabled = value;
      },
      increaseIndex() {
        this.disabledAllButtons(false)
        this.getButton(0);
        this.currantlyIndex+=1; 
      },
      getButton(value){
        if(this.test[this.currantlyIndex].answer==this.test[this.currantlyIndex].option1)
           this.option1_x=value
        
        else if(this.test[this.currantlyIndex].answer==this.test[this.currantlyIndex].option2)
           this.option2_x=value

        else if(this.test[this.currantlyIndex].answer==this.test[this.currantlyIndex].option3)
           this.option3_x=value

        else if(this.test[this.currantlyIndex].answer==this.test[this.currantlyIndex].option4)
           this.option4_x=value
      },
      removeFocus(){
        const focusedElements = document.querySelectorAll(':focus');
        focusedElements.forEach(element => {
          element.blur();
        });
      },
      nextTest() {
        this.disabledAllButtons(true)
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
              this.getButton(data)
              setTimeout(this.increaseIndex, 1000);
            })
            .catch(error=>{console.log(error)})
        }
        else {
          var element = document.getElementById('question')
          element.style.display='none'
          this.getScore()
        }
      },
      selectOption(id, selected_translate){
        this.test[this.currantlyIndex].answer=selected_translate
        var element = document.getElementById(id)
        element.focus();
      },
      getScore(){
        var element = document.getElementById('results')
          element.style.display='block'
        fetch(`http://localhost:8000/check_result/${this.categoryName}`,{
              method:'POST',
              headers: {"Content-Type":"application/json"},
              body: JSON.stringify({questions: this.test})
          })
          .then(resp=>resp.json())
            .then(data=>{
            this.results=data
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
.defaultB{
  padding: 15px;
  font-size: 15px;
  color: black;
  border-width: 2px;
  border-style: solid;
  border-color: blueviolet;
  background-color: azure;
}
.defaultB:focus{
  border-color: steelblue;
  background-color: skyblue;
}
.defaultB:disabled{
  border-color: gray;
  color: gray;
  background-color: whitesmoke;
}
.trueAnswer{
  border-color: greenyellow;
  color: green;
  background-color: lightgreen;
  font-size: 15px;
}
.falseAnswer{
  border-color: palevioletred;
  color: crimson;
  background-color: pink;
  font-size: 15px;
}
#next:disabled{
  border-color: gray;
  color: gray;
  background-color: whitesmoke;
}


#results{
  display: none;
}
#wordAndOptions{
  text-align: center;
}
.options{
  display: grid;
  grid-template-columns: 1fr 1fr;
}
</style>