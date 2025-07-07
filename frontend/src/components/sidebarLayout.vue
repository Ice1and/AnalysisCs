<script setup>var item;

    import { defineProps, ref, onMounted, onUnmounted } from 'vue'
    import { RouterLink, RouterView } from 'vue-router'


    const props = defineProps({
        items: {
            type: Array,
            required: true
        },
        logo: {
            type: String,
            required: true
        },
        logoName: {
            type: String,
            required: true
        }
    })

    const selectButton = ref('home')

    const toggleIsOpen = ref(false)

    const screenWidth = ref(window.innerWidth)

    const updateScreenWidth = () => {
        screenWidth.value = window.innerWidth
        if (screenWidth.value >= 1024) {
            toggleIsOpen.value = false
        }
    }

    const switchToggleStatus = () => {
        toggleIsOpen.value = !toggleIsOpen.value
    }

    onMounted(() => {
        window.addEventListener('resize', updateScreenWidth)
        updateScreenWidth()
    })

    onUnmounted(() => {
        window.removeEventListener('resize', updateScreenWidth)
    })
</script>

<template>
    <div class="relative isolate min-h-svh w-full isolate-auto bg-white lg:bg-zinc-100 flex max-lg:flex-col">
        <!-- sidebar -->
        <!-- fixed 使 nav 脱离文档流 -->
        <nav class="fixed flex flex-col inset-y-0 left-0 w-64 max-lg:hidden">
            <div class="flex flex-col p-4 border-b border-zinc-200 box-border">
                <RouterLink to="/" @click="selectButton = 'home'" class="flex gap-3 items-center p-2 text-left text-base/6 font-medium">
                    <span class="size-7 shrink-0 rounded-full *:rounded-full">
                        <img class="size-full" :src="props.logo" alt="logo">
                    </span>
                    <span class="truncate">{{ props.logoName }}</span>
                </RouterLink>
            </div>
            <div class="flex flex-1 flex-col p-4 overflow-y-auto">
                <div class="flex flex-col gap-1.25">
                    <RouterLink class='relative flex w-full items-center text-left text-base/6 font-medium text-zinc-950 p-2 py-2.5 gap-3 rounded-lg select-none cursor-pointer sm:text-sm/5 sm:py-2 hover:bg-gray-950/5'
                        v-for="item in props.items"
                        :key="item.name"
                        :to="item.path"
                        @click="selectButton = item.name"
                    >
                        <span v-if="selectButton === item.name" class="absolute inset-y-2 -left-4 w-0.5 rounded-full bg-zinc-950"></span>
                        <span class="material-symbols-outlined" style="font-size: 22px;">{{ item.name }}</span>
                        <span class="truncate">{{ item.tooltip }}</span>
                    </RouterLink>
                </div>
            </div>
        </nav>

        <!-- 屏幕宽度小于 lg 时生效 header 汉堡按钮 -->
        <header class="flex px-4 items-center lg:hidden">
            <div class="py-2.5">
                <button @click="switchToggleStatus" class="flex p-2 text-zinc-400 hover:text-gray-800 hover:bg-gray-950/5 rounded-lg select-none cursor-pointer">
                    <span class="material-symbols-outlined" style="font-size: 22px;">menu</span>
                </button>
            </div>
        </header>

        <!-- main -->
        <main class="flex flex-1 flex-col pb-2 lg:min-w-0 lg:pt-2 lg:pr-2 lg:pl-64">
            <div class="grow p-6 lg:rounded-lg lg:bg-white lg:p-10 lg:shadow-xs lg:ring-1 lg:ring-zinc-950/5">
                <div class="mx-auto max-w-6xl">
                    <RouterView></RouterView>
                </div>
            </div>
        </main>

        <!-- 垂直导航，当 toggleIsOpen 为 true 且屏幕宽度小于 lg 时生效 -->
        <div class="lg:hidden">
            <Transition
                enter-active-class="transition-opacity duration-300 ease-in-out"
                leave-active-class="transition-opacity duration-300 ease-in-out"
                enter-from-class="opacity-0"
                leave-to-class="opacity-0"
            >
                <div v-if="toggleIsOpen" @click="switchToggleStatus" class="fixed isolate-auto inset-0 bg-black/30"></div>
            </Transition>

            <Transition
                enter-active-class="transition-transform duration-300 ease-in-out"
                leave-active-class="transition-transform duration-300 ease-in-out"
                enter-from-class="-translate-x-full"
                leave-to-class="-translate-x-full"
            >
                <div v-if="toggleIsOpen" class="fixed inset-y-0 max-w-80 w-full p-2">
                    <div class="flex flex-col h-full bg-white rounded-lg ring-1 ring-zinc-950/5">
                        <div class="px-4 pt-3">
                            <button @click="switchToggleStatus" class="flex p-2 text-zinc-500 hover:text-gray-800 hover:bg-gray-950/5 rounded-lg select-none cursor-pointer">
                                <span class="material-symbols-outlined" style="font-size: 22px">close</span>
                            </button>
                        </div>

                        <nav class="flex flex-col h-full min-h-0">
                            <div class="flex flex-col p-4 border-b border-zinc-950/5 box-border">
                                <button class="flex gap-3 items-center p-2">
                                    <span class="size-7 shrink-0 rounded-full *:rounded-full">
                                        <img class="size-full" :src="props.logo" alt="logo">
                                    </span>
                                    <span class="truncate">{{ props.logoName }}</span>
                                </button>
                            </div>
                            <div class="flex flex-1 flex-col p-4 overflow-y-auto">
                                <div class="flex flex-col gap-1.25">
                                    <RouterLink class="flex w-full text-left text-sm p-2 gap-3 items-center rounded-lg select-none hover:bg-gray-950/5 cursor-pointer"
                                        v-for="item in props.items"
                                        :to="item.path"
                                        :key="item.name"
                                        @click="switchToggleStatus"
                                    >
                                        <span class="material-symbols-outlined" style="font-size: 22px;">{{ item.name }}</span>
                                        <span class="truncate">{{ item.tooltip }}</span>
                                    </RouterLink>
                                </div>
                            </div>
                        </nav>
                    </div>
                </div>
            </Transition>
        </div>

    </div>
</template>

<style scoped>
</style>