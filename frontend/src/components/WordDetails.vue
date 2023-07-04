<template>
    <div>
      <h2>{{currantlyWord.word}}</h2>
      <h3>{{currantlyWord.translate}}</h3>
      <h4>{{currantlyWord.example}}</h4>
      <router-link
            :to="{name: 'wordEdit', params: {categoryName: this.categoryName}}"
            ><button>update</button></router-link>
      <button @click="deleteWord()">delete</button>
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
  </style>