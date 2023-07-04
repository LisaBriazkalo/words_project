<template>
    <div>
      <h1>Words in the {{this.name}} category</h1>
      <div v-for="word in dictionary" :key="word.id">
        <router-link
            :to="{name: 'wordDetails', params: {categoryName: this.name, id:word.id}}"
            >
          <h3>{{word.word}}</h3></router-link>
        <h4>{{word.translate}}</h4>
      </div>
    </div>
  </template>
  
  <script>
  export default{
    data(){
        return {
            dictionary:[],
        }
    },
    props: {
      name: {
        type:[String],
        required: true
      }
    },
    methods:{
      getCategoryData() {
          fetch(`http://localhost:8000/${this.name}`,{
              method:'GET',
              headers: {"Content-Type":"application/json"}
          })
          .then(resp=>resp.json())
          .then(data=>{
              this.dictionary.push(...data)
          })
          .catch(error=>{console.log(error)})
      }
    },
    created() {
      this.getCategoryData()
    }
  }
  </script>
  
  <style>
  </style>