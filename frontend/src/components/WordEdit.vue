<template>
    <div>
    <h1>Edit</h1>
    <form @submit.prevent="editWord">
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
    data(){
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
      },
      id: {
        type:[String],
        required: true
      }
    },
    methods: {
        editWord(){
            if(!this.word || !this.translate || !this.example){
                this.error="Add all fields"
            }else{
                fetch(`http://localhost:8000/${this.categoryName}/${this.id}/`,{
                method:'PUT',
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
    },
    beforeRouteEnter(to, from, next) {
        if(to.params.id!=undefined) {
            fetch(`http://localhost:8000/${to.params.categoryName}/${to.params.id}`,{
              method:'GET',
              headers: {"Content-Type":"application/json"}
          })
          .then(resp=>resp.json())
          .then(data=>{
              return next(vm=>(vm.word=data.word, vm.translate=data.translate, vm.example=data.example))
          })
          .catch(error=>{console.log(error)})
        }
        else {return next()}
    }
  }
  </script>
  
  <style>
  </style>