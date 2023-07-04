<template>
    <div>
    <h1>Home</h1>
    <div v-for="category in categories" :key="category">
        <h3>
            <router-link
            :to="{name: 'dictionary', params: {name:category}}"
            >{{category}}</router-link>
        </h3>

    </div>
    </div>
</template>
  
<script>
export default{
    data(){
        return {
            categories:[],
        }
    }  ,
    methods:{
        getCategories(){
            fetch('http://localhost:8000/',{
                method:'GET',
                headers: {"Content-Type":"application/json"}
            })
            .then(resp=>resp.json())
            .then(data=>{
                this.categories.push(...data)
            })
            .catch(error=>{console.log(error)})
        }
    },
    created() {
        this.getCategories()
    } 
}
</script>
  
<style>
</style>