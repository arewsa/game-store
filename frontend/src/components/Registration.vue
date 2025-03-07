<template>
  <div>
    <section>
      <div
        class="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0"
      >
        <div
          class="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700"
        >
          <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
            <h1
              class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white"
            >
              Create an account
            </h1>
            <form
              class="space-y-4 md:space-y-6"
              @submit.prevent="onClick"
              method="post"
            >
              <div>
                <label
                  for="first_name"
                  class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                  >Your name</label
                >
                <input
                  type="text"
                  name="first_name"
                  id="first_name"
                  required
                  v-model="firstName"
                  class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  placeholder="Ivan"
                />
              </div>
              <div>
                <label
                  for="second_name"
                  class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                  >Your surname</label
                >
                <input
                  type="text"
                  name="second_name"
                  id="second_name"
                  v-model="second_name"
                  required
                  class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  placeholder="Ivanov"
                />
              </div>
              <div>
                <label
                  for="email"
                  class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                  >Your email</label
                >
                <input
                  type="email"
                  name="email"
                  id="email"
                  v-model="mail"
                  required
                  class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  placeholder="name@mail.com"
                />
              </div>
              <div>
                <label
                  for="password"
                  class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                  >Password</label
                >
                <input
                  type="password"
                  name="password"
                  id="password"
                  v-model="password"
                  placeholder="••••••••"
                  required
                  class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                />
              </div>
              <div>
                <label
                  for="confirm-password"
                  class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                  >Confirm password</label
                >
                <input
                  type="password"
                  name="confirm-password"
                  id="confirm-password"
                  required
                  v-model="confirm_password"
                  placeholder="••••••••"
                  class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  :class="{
                    'focus:ring-primary-600 focus:border-primary-600':
                      confirm_password == password,
                    'focus:ring-red-600 focus:border-red-600 ring-red-600 border-red-600':
                      confirm_password != password,
                  }"
                />
                <a
                  v-if="confirm_password != password"
                  class="text-red-600 text-sm"
                >
                  Passwords don't match
                </a>
              </div>
              <button
                type="submit"
                class="w-full text-white bg-primary-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800"
              >
                Create an account
              </button>
              <RouterLink
                to="/login"
                class="text-sm font-light text-gray-500 dark:text-gray-400"
              >
                Already have an account?
                <a
                  class="font-medium text-primary-600 hover:underline dark:text-primary-500"
                  >Login here</a
                >
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

const userExist = ref(false);
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
  const data = await response.json();
  if (data.status == 200) {
    router.push("login");
  } 
  if (data.status == 100) {
    userExist.value = true;
  }
}
</script>

<style scoped></style>
