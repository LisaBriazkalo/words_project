<template>
    <div>
      <h1>Words in the {{this.name}} category</h1>
      <router-link
            :to="{name: 'CreateWord', params: {categoryName: this.name}}"
            ><button>add</button></router-link>
      <div v-for="word in dictionary" :key="word.id">
        <router-link
            :to="{name: 'wordDetails', params: {categoryName: this.name, id:word.id}}"
            >
          <h3>{{word.word}}</h3></router-link>
        <h4>{{word.translate}}</h4>
        <button @click="deleteWord(word.id)">delete</button>
        <hr/>
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
      deleteWord(id) {
        fetch(`http://localhost:8000/${this.name}/${id}`,{
              method:'DELETE',
              headers: {"Content-Type":"application/json"}
          })
          .then(()=>{
            this.$router.go(0);
            })
          .catch(error=>{console.log(error)})
      },
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