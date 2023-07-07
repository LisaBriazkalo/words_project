<template>
    <div>
      <div class="header">
        <router-link class="backB"
          :to="{name: 'dictionary', params: {name:categoryName}}"
              ><button >=</button></router-link>
        <h1>Create a new word</h1>
      </div>
      <div id="newword-form">
        <form @submit.prevent="insertWord">
          <input 
          type="text"
          placeholder="enter your word"
          v-model="word"
          class="long-input"
          />
          <input
          type="text"
          placeholder="enter translate"
          v-model="translate"
          class="long-input"
          />
          <textarea rows="10"
          type="text"
          placeholder="enter example"
          v-model="example"
          class="long-input"
          ></textarea>
          <button>ok</button>
        </form>
      </div>
      <div v-if="error">
        <strong>error</strong>
      </div>
    </div>
  </template>
  
  <script>
  export default{
    data() {
        return{
            word:null,
            translate:null,
            example:null,
            error:null
        }
    },
    props: {
      categoryName: {
        type:[String],
        required: true
      }
    },
    methods:{
        insertWord(){
            if(!this.word || !this.translate || !this.example){
                this.error="Add all fields"
            }else{
                fetch(`http://localhost:8000/post_new_word/${this.categoryName}`,{
                method:'POST',
                headers: {"Content-Type":"application/json"},
                body: JSON.stringify({word: this.word, translate: this.translate, example:this.example})
            })
            .then(resp=>resp.json())
            .then(()=>{
                this.$router.push({
                    name:'dictionary',
                    params: { name: this.categoryName }
                })
            })
            .catch(error=>{console.log(error)})
            }
        }
    }
  }
  </script>
  
  <style>
  #newword-form{
    margin: 5%;
    padding-left: 5%;
    padding-right: 5%;
  }


  </style>