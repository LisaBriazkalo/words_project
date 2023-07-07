<template>
    <div>
    <h1>Home</h1>
    <div v-for="category in categories" :key="category">
        <div class="category-plate">
            <h3>
                <router-link 
                :to="{name: 'dictionary', params: {name:category}}"
                >{{category}}</router-link>
                <div :id="'category-rename-' + category" class="category-rename">
                    <form @submit.prevent="editName">
                    <input  
                    placeholder="enter new name" 
                    v-model="newName" 
                    class="short-input"/>
                    <button class="button-delete" type="submit">ok</button>
                    </form>
                    <div v-if="error">
                    <strong>error</strong>
                    </div>
                </div>
            </h3>
            <p><button  @click="openEditForm(category)">rename</button></p>
            <p><button @click="deleteCategory(category)">x</button></p>
        </div>
        <hr/>
    </div>
    <div id="add-new-category">
    <input
        type="text"
        placeholder="new-category"
        v-model="newCategory"
        class="short-input"
        />
    <button class="button-delete" @click="createCategory(this.newCategory)">+</button>
    </div>
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
    },
    methods:{
        editName(){
            if(!this.newName){
                this.error="Add all fields"
            }else{
                fetch(`http://localhost:8000/update_collection_name/${this.oldName}/`,{
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
            var element = document.getElementById('category-rename-' + this.oldName);
            element.style.display = "flex";
            
        },
        deleteCategory(category) {
            fetch(`http://localhost:8000/delete_collection/${category}/`,{
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
                fetch('http://localhost:8000/post_new_category',{
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
            fetch('http://localhost:8000/get_collections_names',{
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
#add-new-category{
    display: block;
    margin-top: 5px;
    margin-bottom: 5px;
}

</style>