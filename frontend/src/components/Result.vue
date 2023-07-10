<template>
    <div>
        <h2>name {{ categoryName }}</h2>
        <h3>score: {{ score }}</h3>
      
    </div>
  </template>
  
  <script>
  export default{
    props: {
        categoryName: {
            type:[String],
            required: true
        }
        // ,
        // score: {
        //     type:[Number],
        //     required: true
        // }
        // ,
        // failing:{
        //     type:[Number],
        //     required: true
        // },
        // numberOfQuestions:{
        //     type:[Number],
        //     required: true
        // }
    }
   
  }
  </script>
  
<style>

</style>