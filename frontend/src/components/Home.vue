<template>
    <div>
    <h1>Home</h1>
    <div v-for="category in categories" :key="category">
        <h3>
            <router-link
            :to="{name: 'dictionary', params: {name:category}}"
            >{{category}}</router-link>
            <div id="rename-category">
                <input  placeholder="enter new name"/>
                <button>ok</button>
                <button>x</button>
            </div>
                <button @click="editCategory()">rename</button>
            <button @click="deleteCategory(category)">delete</button>
        </h3>
        <hr/>
    </div>
    <input
        type="text"
        placeholder="new-category"
        v-model="newCategory"
        />
    <button @click="createCategory(this.newCategory)">add</button>
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
        editCategory() {
            var element = document.getElementById("rename-category");
            element.style.display = "flex";

        },
        deleteCategory(category) {
            fetch(`http://localhost:8000/${category}/`,{
              method:'DELETE',
              headers: {"Content-Type":"application/json"}
          })
          .then(()=>{
            this.$router.go(0);
            })
          .catch(error=>{console.log(error)})
        },
        createCategory(newCategory) {
            if(!newCategory){
                this.error="Add all fields"
            }else{
                fetch('http://localhost:8000/',{
                method:'POST',
                headers: {"Content-Type":"application/json"},
                body: JSON.stringify({name: newCategory})
            })
            .then(resp=>resp.json())
            .then(()=>{
            this.$router.go(0);
            })
            .catch(error=>{console.log(error)})
            }
        },
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
#rename-category{
    display: none;
}
</style>