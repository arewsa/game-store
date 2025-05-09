<template>
  <div class="mx-auto max-w-md rounded-lg bg-white p-6 shadow-md">
    <h2 class="mb-6 text-center text-2xl font-bold">Добавить товар</h2>

    <form @submit.prevent="submitForm" class="space-y-4">
      <div>
        <label class="mb-1 block text-sm font-medium text-gray-700">Image</label>
        <div class="flex w-full items-center justify-center">
          <label
            class="flex h-32 w-full cursor-pointer flex-col items-center justify-center rounded-lg border-2 border-dashed border-gray-300 bg-gray-50 hover:bg-gray-100"
          >
            <div class="flex flex-col items-center justify-center pb-6 pt-5">
              <template v-if="!imagePreview">
                <svg class="mb-3 h-8 w-8 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"
                  ></path>
                </svg>
                <p class="mb-2 text-sm text-gray-500">Click to load picture</p>
              </template>
              <img v-else :src="imagePreview" class="h-24 rounded object-cover" alt="Предпросмотр" />
            </div>
            <input type="file" class="hidden" accept="image/*" @change="handleImageUpload" />
          </label>
        </div>
      </div>

      <div>
        <label for="title" class="mb-1 block text-sm font-medium text-gray-700">Name</label>
        <input
          id="title"
          v-model="form.title"
          type="text"
          class="w-full rounded-md border border-gray-300 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
          placeholder="Insert name"
          required
        />
      </div>

      <div>
        <label for="price" class="mb-1 block text-sm font-medium text-gray-700">Price</label>
        <div class="relative">
          <input
            id="price"
            v-model="form.price"
            type="number"
            min="0"
            step="0.01"
            class="w-full rounded-md border border-gray-300 py-2 pl-8 pr-3 focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="0.00"
            required
          />
          <span class="absolute left-3 top-2.5 text-gray-500">$</span>
        </div>
      </div>

      <button
        type="submit"
        class="w-full rounded-md bg-blue-600 px-4 py-2 font-medium text-white transition duration-200 hover:bg-blue-700"
      >
        Add Product
      </button>
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { fetchWithCredentials } from "../services/auth";
import { fromJSON } from "postcss";

const form = ref({
  title: "",
  price: 0,
  image: null,
});

const imagePreview = ref(null);

const handleImageUpload = (event) => {
  const file = event.target.files[0];
  if (file) {
    form.value.image = file;
    const reader = new FileReader();
    reader.onload = (e) => {
      imagePreview.value = e.target.result;
    };
    reader.readAsDataURL(file);
  }
};

const submitForm = () => {
  const productData = {
    name: form.value.title,
    price: form.value.price,
    img: form.value.image != null ? form.value.image.name : "DarkSouls3.png",
    product: "game",
  };
  fetchWithCredentials("http://localhost:8000/products", {  
    method: "POST",
    credentials: "include",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(productData),
  });
  if (form.value.image) {
    fetchWithCredentials(`http://localhost:9000/product-image/${form.value.image.name}`, {
      method: "PUT",
      body: form.value.image,
      headers: { "Content-Type": form.value.image.type },
    });
  }
  form.value = { title: "", price: "", image: null };
  imagePreview.value = null;
};
</script>
