<template>
    <div>
      <form @submit.prevent="insertWord">
        <input
        type="text"
        placeholder="enter your word"
        v-model="word"
        />
        <br/>
        <input
        type="text"
        placeholder="enter translate"
        v-model="translate"
        /><br/>
        <textarea rows="10"
        type="text"
        placeholder="enter example"
        v-model="example"
        ></textarea>
        <br/>
        <button>ok</button>
      </form>
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
                fetch(`http://localhost:8000/${this.categoryName}`,{
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
  </style>