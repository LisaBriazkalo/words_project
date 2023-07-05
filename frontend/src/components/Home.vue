<template>
    <div>
    <h1>Home</h1>
    <div v-for="category in categories" :key="category">
        <h3>
            <router-link id="category-label"
            :to="{name: 'dictionary', params: {name:category}}"
            >{{category}}</router-link>
            <div id="category-rename">
                <form @submit.prevent="editName">
                <input  placeholder="enter new name" v-model="newName" />
                <button type="submit">ok</button>
                <button @click="closeEditForm">x</button>
                </form>
                <div v-if="error">
                <strong>error</strong>
                </div>
            </div>
                <button id="category-rename-button" @click="openEditForm(category)">rename</button>
            <button id="category-delete-button" @click="deleteCategory(category)">delete</button>
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
            oldName:null,
            newName:null,
            error:null
        }
    }  ,
    methods:{
        editName(){
            if(!this.newName){
                this.error="Add all fields"
            }else{
                fetch(`http://localhost:8000/${this.oldName}/`,{
                method:'PUT',
                headers: {"Content-Type":"application/json"},
                body: JSON.stringify({name: this.newName})
            })
            .then(resp=>resp.json())
            .then(()=>{
            this.$router.go(0);
            })
            .catch(error=>{console.log(error)})
            }
        },
        openEditForm(oldname) {
            this.newName=oldname
            this.oldName=oldname
            var element = document.getElementById("category-rename");
            element.style.display = "flex";
            element = document.getElementById("category-label");
            element.style.display = "none";
            element = document.getElementById("category-rename-button");
            element.style.display = "none";
            element = document.getElementById("category-delete-button");
            element.style.display = "none";
        },
        closeEditForm() {
            var element = document.getElementById("category-rename");
            element.style.display = "none";
            element = document.getElementById("category-label");
            element.style.display = "inline";
            element = document.getElementById("category-rename-button");
            element.style.display = "inline";
            element = document.getElementById("category-delete-button");
            element.style.display = "inline";
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
#category-rename{
    display: none;
}
</style>