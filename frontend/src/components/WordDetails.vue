<template>
    <div>
      <div class="header">
        <router-link class="backB"
          :to="{name: 'dictionary', params: {name:categoryName}}"
              ><button >=</button></router-link>
        <h1>Word details</h1>
      </div>
      <div id="word-details">
      <div id="word-card">
        <h1 id="word-label">{{currantlyWord.word}}</h1>
        <h3 id="translate-label">{{currantlyWord.translate}}</h3>
        <h4 id="example-label">example: {{currantlyWord.example}}</h4>
      </div>
      <router-link
            :to="{name: 'wordEdit', params: {categoryName: this.categoryName}}"
            ><button>update</button></router-link>
      <button @click="deleteWord()">delete</button>
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
      },
      id: {
        type:[String],
        required: true
      }
    },
    methods:{
      deleteWord() {
        fetch(`http://localhost:8000/${this.categoryName}/${this.id}`,{
              method:'DELETE',
              headers: {"Content-Type":"application/json"}
          })
          .then(()=>{
                this.$router.push({
                    name:'dictionary',
                    params: { name: this.categoryName }
                })
            })
          .catch(error=>{console.log(error)})
      },
      getWordData() {
          fetch(`http://localhost:8000/${this.categoryName}/${this.id}`,{
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
  #word-card{
    border-width: 4px;
    border-style: solid;
    border-color: blueviolet;
    padding-left: 5%;
    padding-right: 5%;
  }
  #example-label{
    color: gray;
  }
  #word-label{
    font-size: 40px;
    line-height: 0.4;
  }
  #translate-label{
    line-height: 0.4;
  }
  #word-details{
    margin: 5%;
  }
  </style>