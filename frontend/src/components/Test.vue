<template>
    <div>
        <div class="header">
        <router-link class="backB"
          :to="{name: 'dictionary', params: {name:this.categoryName}}"
              ><button >=</button></router-link>
        <h1>Test task</h1>
      </div>
      <div>
        <h2>{{ currantlyWord.word }}</h2>
        <button class="button1" onclick="isRightAnswer(event)">{{ currantlyWord.translate0 }}</button>
        <button class="button1">{{ currantlyWord.translate1 }}</button>
        <button class="button1">{{ currantlyWord.translate2 }}</button>
        <button class="button1">{{ currantlyWord.translate3 }}</button>
      </div>
    </div>
  </template>
  
  <script>
  export default{
    data(){
        return {
            currantlyWord:{},
        }
    },
    props: {
      categoryName: {
        type:[String],
        required: true
      }
    },
    methods:{
        getWordData() {
          fetch(`http://localhost:8000/${this.categoryName}/fourWords/`,{
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

</style>