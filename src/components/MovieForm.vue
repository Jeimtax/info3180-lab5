<template>
    <div class="cointainer mt-4">
        <h1>Upload Form</h1>


        <div v-if="successMessage" class="alert alert-success">
            {{ successMessage }}
        </div>

        <div v-if="errorMessages.length > 0" class="alert alert-danger">
            <ul>
                <li v-for="error in errorMessages" :key="error">{{ error }}</li>
            </ul>
        </div>

        <form id="movieForm" @submit.prevent="saveMovie" enctype="multipart/form-data">
            <div class="form-group mb-3">
                <label for="title" class="form-label">Movie Title</label>
                <input type="text" name="title" class="form-control"/>
            </div>
            
            <div class="form-group mb-3">
                <label for="description" class="form-label">Description</label>
                <textarea name="description" class="form-control"></textarea>
            </div>

            <div class="form-group mb-3">
                <label for="poster" class="form-label">Photo Upload</label>
                <input type="file" name="poster" class="form-control"/>
            </div>

            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

let successMessage = ref("");
let errorMessages = ref([]);


onMounted(() => {
    getCsrfToken();
});


function saveMovie(){
    let movieForm = document.getElementById('movieForm');
    let form_data = new FormData(movieForm);

    fetch("/api/v1/movies", {
        method: 'POST',
        body: form_data,
        headers: {
            'X-CSRFToken': csrf_token.value
        }   
    })
    
    
    .then(function (response) {
        return response.json();
    })

    .then(function (data) {
        if (data.errors) {
            errorMessages.value = data.errors;
            successMessage.value = "";
        } else {
            successMessage.value = data.message;
            errorMessages.value = [];
        }
    })

    .catch(function (error) {
        console.log(error);
    });
}

</script>