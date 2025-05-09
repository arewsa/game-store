<template>
  <div>
    <section>
      <div class="mx-auto flex flex-col items-center justify-center px-6 py-8 md:h-screen lg:py-0">
        <div
          class="w-full rounded-lg bg-white shadow dark:border dark:border-gray-700 dark:bg-gray-800 sm:max-w-md md:mt-0 xl:p-0"
        >
          <div class="space-y-4 p-6 sm:p-8 md:space-y-6">
            <h1 class="text-xl font-bold leading-tight tracking-tight text-gray-900 dark:text-white md:text-2xl">
              Create an account
            </h1>
            <form class="space-y-4 md:space-y-6" @submit.prevent="onClick" method="post">
              <div>
                <label for="first_name" class="mb-2 block text-sm font-medium text-gray-900 dark:text-white"
                  >Your name</label
                >
                <input
                  type="text"
                  name="first_name"
                  id="first_name"
                  required
                  v-model="firstName"
                  class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-primary-600 focus:ring-primary-600 dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:placeholder-gray-400 dark:focus:border-blue-500 dark:focus:ring-blue-500"
                  placeholder="Ivan"
                />
              </div>
              <div>
                <label for="second_name" class="mb-2 block text-sm font-medium text-gray-900 dark:text-white"
                  >Your surname</label
                >
                <input
                  type="text"
                  name="second_name"
                  id="second_name"
                  v-model="second_name"
                  required
                  class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-primary-600 focus:ring-primary-600 dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:placeholder-gray-400 dark:focus:border-blue-500 dark:focus:ring-blue-500"
                  placeholder="Ivanov"
                />
              </div>
              <div>
                <label for="email" class="mb-2 block text-sm font-medium text-gray-900 dark:text-white"
                  >Your email</label
                >
                <input
                  type="email"
                  name="email"
                  id="email"
                  v-model="mail"
                  required
                  class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-primary-600 focus:ring-primary-600 dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:placeholder-gray-400 dark:focus:border-blue-500 dark:focus:ring-blue-500"
                  placeholder="name@mail.com"
                />
              </div>
              <div>
                <label for="password" class="mb-2 block text-sm font-medium text-gray-900 dark:text-white"
                  >Password</label
                >
                <input
                  type="password"
                  name="password"
                  id="password"
                  v-model="password"
                  placeholder="••••••••"
                  required
                  class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-primary-600 focus:ring-primary-600 dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:placeholder-gray-400 dark:focus:border-blue-500 dark:focus:ring-blue-500"
                />
              </div>
              <div>
                <label for="confirm-password" class="mb-2 block text-sm font-medium text-gray-900 dark:text-white"
                  >Confirm password</label
                >
                <input
                  type="password"
                  name="confirm-password"
                  id="confirm-password"
                  required
                  v-model="confirm_password"
                  placeholder="••••••••"
                  class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:placeholder-gray-400 dark:focus:border-blue-500 dark:focus:ring-blue-500"
                  :class="{
                    'focus:border-primary-600 focus:ring-primary-600': confirm_password == password,
                    'border-red-600 ring-red-600 focus:border-red-600 focus:ring-red-600': confirm_password != password,
                  }"
                />
                <a v-if="confirm_password != password" class="text-sm text-red-600"> Passwords don't match </a>
              </div>
              <button
                type="submit"
                class="w-full rounded-lg bg-primary-600 px-5 py-2.5 text-center text-sm font-medium text-white hover:bg-primary-700 focus:outline-none focus:ring-4 focus:ring-primary-300 dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800"
              >
                Create an account
              </button>
              <RouterLink to="/login" class="text-sm font-light text-gray-500 dark:text-gray-400">
                Already have an account?
                <a class="font-medium text-primary-600 hover:underline dark:text-primary-500">Login here</a>
              </RouterLink>
            </form>
          </div>
        </div>
      </div>
    </section>
    <Toast
      :message="'You\'re are already registered!'"
      :description="' Maybe you just need to log in?'"
      v-model="userExist"
    ></Toast>
    <Toast
      :message="`Welcome ${data.name} ${data.surname}!`"
      :description="' Now you can log in to your account. Wait a second'"
      v-model="userReg"
    ></Toast>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { RouterLink } from "vue-router";
import router from "../router/router";
import Toast from "./Toast.vue";

const firstName = ref("");
const second_name = ref("");
const mail = ref("");
const password = ref("");
const confirm_password = ref("");
const data = ref({ name: "", surname: "" });

const userExist = ref(false);
const userReg = ref(false);
const url = "http://localhost:8000/users";

async function onClick() {
  const formData = {
    name: firstName.value,
    surname: second_name.value,
    mail: mail.value,
    password: password.value,
  };
  const response = await fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(formData),
  });
  data.value = await response.json();
  if (response.status == 200) {
    userReg.value = true;
    await new Promise((f) => setTimeout(f, 3000));
    router.push("login");
  } else if (response.status == 400) {
    userExist.value = true;
    await new Promise((f) => setTimeout(f, 3000));
    userExist.value = false;
  }
}
</script>

<style scoped></style>
