<script setup>
    import { defineProps } from 'vue';

    const prop = defineProps({
        headers: {
            type: Array,
            required: true
        }
    })
</script>

<template>
    <div class="inline-block min-w-full align-middle">
        <table class="min-w-full text-left text-sm/6 text-zinc-950">
            <thead class="text-zinc-500">
                <tr>
                    <th class="border-b border-b-zinc-950/10 px-4 py-2 font-medium" v-for="header in headers"></th>
                </tr> 
            </thead>
        </table>
    </div>
</template>