<template>
  <div class="flex w-full justify-center p-6 gap-4 duration-500 min-h-[98vh]">
    <div class="fixed w-64 left-6">
      <SidebarMain />
    </div>
    <div
      class="ml-72 w-5/6 bg-frameBackground rounded-xl border-[0.5px] border-neutral-600 duration-500"
    >
      <div class="flex flex-col gap-3 h-full p-4">
        <!-- Ключевые слова -->
        <div class="flex items-start w-full">
          <p class="text-activeText w-1/6">Ключевые слова</p>
          <input
            class="rounded-md w-4/6 h-12 placeholder:pl-2.5 placeholder:text-sm border-2 border-neutral-300 shadow-sm"
            placeholder="Например: сталь, 36.40.11.133"
          />
        </div>
        <!-- Исключить слова -->
        <div class="flex items-center w-full">
          <p class="text-activeText w-1/6">Исключить слова</p>
          <input
            class="rounded-md w-4/6 h-8 border-2 border-neutral-300 shadow-sm"
          />
        </div>
        <!-- Цена -->
        <div class="flex items-center w-full">
          <p class="text-activeText w-1/6">Цена</p>
          <input
            class="rounded-md w-1/6 h-10 placeholder:pl-2.5 placeholder:text-sm border-2 border-neutral-300 shadow-sm"
            placeholder="0"
          />
          <div class="pl-1">
            <svg
              fill="currentColor"
              viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg"
              class="w-6 h-6 text-neutral-100 duration-300"
            >
              <path
                id="primary"
                d="M14,11H9V3h5a4,4,0,0,1,4,4h0A4,4,0,0,1,14,11ZM9,3V21M6,11H9"
                :style="{ stroke: isDarkMode ? 'white' : '#000000' }"
                style="
                  fill: none;
                  stroke-linecap: round;
                  stroke-linejoin: round;
                  stroke-width: 2;
                "
              ></path>
              <line
                id="primary-2"
                data-name="primary"
                x1="6"
                y1="15"
                x2="15"
                y2="15"
                :style="{ stroke: isDarkMode ? 'white' : '#000000' }"
                style="
                  fill: none;
                  stroke-linecap: round;
                  stroke-linejoin: round;
                  stroke-width: 2;
                "
              ></line>
            </svg>
          </div>
          <p class="text-activeText px-4">—</p>
          <input
            class="rounded-md w-1/6 h-10 placeholder:pl-2.5 placeholder:text-sm border-2 border-neutral-300 shadow-sm"
            placeholder="0"
          />
          <div class="pl-1">
            <svg
              fill="currentColor"
              viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg"
              class="w-6 h-6 text-neutral-100 duration-300"
            >
              <path
                id="primary"
                d="M14,11H9V3h5a4,4,0,0,1,4,4h0A4,4,0,0,1,14,11ZM9,3V21M6,11H9"
                :style="{ stroke: isDarkMode ? 'white' : '#000000' }"
                style="
                  fill: none;
                  stroke-linecap: round;
                  stroke-linejoin: round;
                  stroke-width: 2;
                "
              ></path>
              <line
                id="primary-2"
                data-name="primary"
                x1="6"
                y1="15"
                x2="15"
                y2="15"
                :style="{ stroke: isDarkMode ? 'white' : '#000000' }"
                style="
                  fill: none;
                  stroke-linecap: round;
                  stroke-linejoin: round;
                  stroke-width: 2;
                "
              ></line>
            </svg>
          </div>
        </div>
        <!-- Дата -->
        <div class="flex items-center w-full">
          <p class="text-activeText w-1/6">Опубликовано</p>
          <input
            class="rounded-md w-1/6 h-10 placeholder:pl-2.5 placeholder:text-sm border-2 border-neutral-300 shadow-sm"
            placeholder="22.03.2024"
          />
          <p class="pl-1">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke-width="1.5"
              stroke="currentColor"
              class="w-6 h-6 dark:text-neutral-100 text-neutral-900 duration-300"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M6.75 3v2.25M17.25 3v2.25M3 18.75V7.5a2.25 2.25 0 0 1 2.25-2.25h13.5A2.25 2.25 0 0 1 21 7.5v11.25m-18 0A2.25 2.25 0 0 0 5.25 21h13.5A2.25 2.25 0 0 0 21 18.75m-18 0v-7.5A2.25 2.25 0 0 1 5.25 9h13.5A2.25 2.25 0 0 1 21 11.25v7.5m-9-6h.008v.008H12v-.008ZM12 15h.008v.008H12V15Zm0 2.25h.008v.008H12v-.008ZM9.75 15h.008v.008H9.75V15Zm0 2.25h.008v.008H9.75v-.008ZM7.5 15h.008v.008H7.5V15Zm0 2.25h.008v.008H7.5v-.008Zm6.75-4.5h.008v.008h-.008v-.008Zm0 2.25h.008v.008h-.008V15Zm0 2.25h.008v.008h-.008v-.008Zm2.25-4.5h.008v.008H16.5v-.008Zm0 2.25h.008v.008H16.5V15Z"
              />
            </svg>
          </p>
          <p class="text-activeText px-4">—</p>
          <input
            class="rounded-md w-1/6 h-10 placeholder:pl-2.5 placeholder:text-sm border-2 border-neutral-300 shadow-sm"
            placeholder="23.03.2024"
          />
          <p class="pl-1">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke-width="1.5"
              stroke="currentColor"
              class="w-6 h-6 dark:text-neutral-100 text-neutral-900 duration-300"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M6.75 3v2.25M17.25 3v2.25M3 18.75V7.5a2.25 2.25 0 0 1 2.25-2.25h13.5A2.25 2.25 0 0 1 21 7.5v11.25m-18 0A2.25 2.25 0 0 0 5.25 21h13.5A2.25 2.25 0 0 0 21 18.75m-18 0v-7.5A2.25 2.25 0 0 1 5.25 9h13.5A2.25 2.25 0 0 1 21 11.25v7.5m-9-6h.008v.008H12v-.008ZM12 15h.008v.008H12V15Zm0 2.25h.008v.008H12v-.008ZM9.75 15h.008v.008H9.75V15Zm0 2.25h.008v.008H9.75v-.008ZM7.5 15h.008v.008H7.5V15Zm0 2.25h.008v.008H7.5v-.008Zm6.75-4.5h.008v.008h-.008v-.008Zm0 2.25h.008v.008h-.008V15Zm0 2.25h.008v.008h-.008v-.008Zm2.25-4.5h.008v.008H16.5v-.008Zm0 2.25h.008v.008H16.5V15Z"
              />
            </svg>
          </p>
        </div>
        <!-- Кнопка найти -->
        <div class="flex">
          <button
            type="button"
            class="text-activeText px-5 py-2 rounded-md bg-blue-900 text-neutral-100 shadow-sm"
          >
            Найти
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import AssistantCategoryService from "./AssistantCategoryService.vue";
import AssistantCategoryServiceSection from "./AssistantCategoryServiceSection.vue";
import BaseIcon from "./BaseIcon.vue";
import SidebarMain from "./SidebarMain.vue";
export default {
  components: {
    AssistantCategoryService,
    BaseIcon,
    AssistantCategoryServiceSection,
    SidebarMain,
  },

  data() {
    return {
      questionQuery: "",
    };
  },

  methods: {
    askQuestion() {
      console.log(this.questionQuery);
      axios
        .post(
          `http://${process.env.VUE_APP_ASSISTANT_SEARCH_IP}/assistant/llamaSupportStream?text=${this.questionQuery}`,
          { responseType: "stream" }
        )
        .then((response) => {
          console.log(response.data);
        });
    },
  },

  computed: {
    isDarkMode() {
      return this.$store.state.darkMode;
    },
  },
};
</script>
<style>
.rainbows {
  position: relative;
}

@keyframes rainbow {
  0% {
    color: white;
  }

  33% {
    color: blue;
  }

  66% {
    color: red;
  }

  100% {
    color: white;
  }
}

.owl {
  position: absolute;
  width: 40px;
  height: 40px;
  background-image: url("https://freesvg.org/img/1531730612.png");
  background-size: cover;
  animation: fly-around 5s ease-in-out infinite;
}

@keyframes fly-around {
  0% {
    left: 40px;
    top: 0px;
  }

  25% {
    left: 40px;
    top: 20px;
  }

  50% {
    left: 55px;
    top: 5px;
  }

  75% {
    left: 25;
    top: 15px;
  }

  100% {
    left: 40px;
    top: 0px;
  }
}

.custom-scrollbar {
  scrollbar-width: thin;
  scrollbar-color: #535353 #272727;
}

.custom-scrollbar::-webkit-scrollbar {
  width: 5px;
}

.custom-scrollbar::-webkit-scrollbar-track {
  background: #27272700;
}

.custom-scrollbar::-webkit-scrollbar-thumb {
  background-color: #535353;
  border-radius: 12px;
}

.custom-scrollbar::-webkit-scrollbar-thumb:hover {
  background-color: #323232;
}
</style>
