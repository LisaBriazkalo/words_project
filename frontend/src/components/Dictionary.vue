<template>
    <div>
      <div class="header">
        <router-link class="backB"
              :to="{name: 'home'}"
              ><button >=</button></router-link>
        <h1>Words in the {{this.name}} category</h1>
      </div>
      <div v-for="word in dictionary" :key="word.id" >
        <div class="word-translate">
          <router-link
              :to="{name: 'wordDetails', params: {categoryName: this.name, id:word.id}}"
              >
          <h3>{{word.word}}</h3></router-link>
          <h4>{{word.translate}}</h4>
          <p><button @click="deleteWord(word.id)" >x</button></p>
        </div>
        <hr/>
      </div>
      <div class="addB">
      <router-link 
            :to="{name: 'createWord', params: {categoryName: this.name}}"
            ><button >+</button></router-link>
      <router-link 
            :to="{name: 'test', params: {categoryName: this.name}}"
            ><button >t</button></router-link></div>
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
.addB{
  display: flex;
  justify-content:  center;
}
  </style>