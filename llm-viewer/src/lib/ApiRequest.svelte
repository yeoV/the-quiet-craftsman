<script lang="ts">
    import type { File } from 'svelte/types/runtime/index';
    let {
        modelUrl,
        prompt,
        uploadedImage,
        selectedModel,
        onResponse,
        modelName,
    } = $props();

    let isLoading = $state(false);
    
    async function encodeImageToBase64(file: File): Promise<string> {
        return new Promise((resolve, reject) => {
            const reader = new FileReader();
            reader.readAsDataURL(file);
            reader.onload = () => resolve(reader.result as string);
            reader.onerror = (error) => reject(error);
        });
    }

    async function getRequestBody() {
        if (!prompt) {
            throw new Error('Prompt is required');
        }

        const baseRequest = {
            model: modelName,
            messages: [
                {
                    role: 'user',
                    content: [
                        {
                            type: 'text',
                            text: prompt,
                        },
                    ],
                },
            ],
        };

        if (selectedModel === 'image' && uploadedImage) {
            const imageUrl = await encodeImageToBase64(uploadedImage);
            baseRequest.messages[0].content.push({
                type: 'image_url',
                image_url: imageUrl,
            });
        }

        return JSON.stringify(baseRequest);
    }

    async function getApiEndpoint() {
        return `${modelUrl}/v1/response`;
        // return `${modelUrl}/engines/llama.cpp/v1/chat/completions`;
    }

    async function getHeaders() {
        return {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        };
    }

    async function sendRequest() {
        isLoading = true;
        try {
            const endpoint = await getApiEndpoint();
            const body = await getRequestBody();
            const headers = await getHeaders();
            
            // debug
            console.log('Request Details:');
            console.log('Endpoint:', endpoint);
            console.log('Body:', body);
            console.log('Headers:', headers);
            console.log('Model Name:', modelName);
            
            const response = await fetch('/api/proxy', {
                method: 'POST',
                headers,
                body: JSON.stringify({
                    target: endpoint,
                    init: {
                        method: 'POST',
                        headers,
                        body,
                    },
                }),
            });

            if (!response.ok) {
                const errorData = await response.json().catch(() => null);
                onResponse?.(`API Error: ${response.status} ${response.statusText}\n${errorData ? JSON.stringify(errorData, null, 2) : 'No error details available'}`);
                return; 
            }

            const data = await response.json();
            if (selectedModel === 'image') {    
                onResponse?.(data.result || 'No response received');
            } else {
                onResponse?.(data.choices?.[0]?.message?.content || 'No response received');
            }
        } catch (error) {
            console.error('API Request Error:', error);
            onResponse?.(error instanceof Error ? error.message : 'Unknown error occurred');
        } finally {
            isLoading = false;
        }
    }

    function handleRequest() {
        sendRequest();
    }
</script>

<button
    type="button"
    onclick={handleRequest}
    class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded disabled:opacity-50 disabled:cursor-not-allowed"
    disabled={isLoading}
>
    {isLoading ? 'Loading...' : 'Send'}
</button>

