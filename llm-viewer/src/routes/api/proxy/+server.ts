import type { RequestHandler } from "@sveltejs/kit";

export const POST: RequestHandler = async ({ request }) => {
    const { target, init } = await request.json();

    // verify allow domain 
    const ALLOWED_ORIGIN = [
        "http://localhost:12434",

    ];
    if (!ALLOWED_ORIGIN.some(origin => target.startsWith(origin))) {
        return new Response('Forbidden target domain', { status: 403 });
    }

    const response = await fetch(target, init);
    const body = await response.arrayBuffer();
    const headers = new Headers(response.headers);

    headers.set('Access-Control-Allow-Origin', '*');

    return new Response(body, { status: response.status, headers });
}