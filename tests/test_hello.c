#include <unity.h>

// Required by Unity — called before/after each test.
// Empty for now; we'll use these for fixtures later.
void setUp(void) {}
void tearDown(void) {}

void test_addition_works(void) {
    TEST_ASSERT_EQUAL_INT(4, 2 + 2);
}

void test_strings_compare(void) {
    TEST_ASSERT_EQUAL_STRING("hello", "hello");
}

int main(void) {
    UNITY_BEGIN();
    RUN_TEST(test_addition_works);
    RUN_TEST(test_strings_compare);
    return UNITY_END();
}

